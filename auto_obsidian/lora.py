# @title Prepare function for Load and text generation { display-mode: "form" }
from .folders import LLM_FOLDER
from .llm import LLM_Base

import torch
import transformers
from transformers import (
    AutoModelForCausalLM, AutoModel,
    AutoTokenizer, LlamaTokenizer,
    GenerationConfig
)
import re
import os
import json
import gc
import peft
import sys

loaded_models = dict()
loaded_tokenizers = dict()

MAX_TOKEN_SIZE=3072
# CACHE_DIR=google_drive_data_directory_path

def get_torch():
    return torch
def get_device():
    if torch.cuda.is_available():
        return "cuda"
    else:
        return "cpu"
def get_peft_model_class():
    return peft.PeftModel
def _get_model_from_pretrained(
        model_class, model_name,
        from_tf=False, force_download=False):
    torch = get_torch()
    device = get_device()

    if device == "cuda":
        return model_class.from_pretrained(
            model_name,
            torch_dtype=torch.float16,
            # device_map="auto",
            # ? https://github.com/tloen/alpaca-lora/issues/21
            device_map={'': 0},
            from_tf=from_tf,
            force_download=force_download,
            trust_remote_code=True,
            cache_dir=LLM_FOLDER
        )
    else:
        return model_class.from_pretrained(
            model_name,
            device_map={"": device},
            low_cpu_mem_usage=True,
            from_tf=from_tf,
            force_download=force_download,
            trust_remote_code=True,
            cache_dir=LLM_FOLDER
        )
def get_tokenizer(base_model_name):
    if base_model_name in loaded_tokenizers:
        return loaded_tokenizers[base_model_name]

    try:
        tokenizer = AutoTokenizer.from_pretrained(
            base_model_name,
            trust_remote_code=True
        )
    except Exception as e:
        if 'LLaMATokenizer' in str(e) or 'LLamaTokenizer' in str(e):
            tokenizer = LlamaTokenizer.from_pretrained(
                base_model_name,
                trust_remote_code=True
            )
        else:
            raise e

    loaded_tokenizers[base_model_name] = tokenizer

    return tokenizer
def get_new_base_model(base_model_name):
    model_class = AutoModelForCausalLM
    from_tf = False
    force_download = False
    has_tried_force_download = False
    while True:
        try:
            model = _get_model_from_pretrained(
                model_class,
                base_model_name,
                from_tf=from_tf,
                force_download=force_download
            )
            break
        except Exception as e:
            if 'from_tf' in str(e):
                print(
                    f"Got error while loading model {base_model_name} with AutoModelForCausalLM: {e}.")
                print("Retrying with from_tf=True...")
                from_tf = True
                force_download = False
            elif model_class == AutoModelForCausalLM:
                print(
                    f"Got error while loading model {base_model_name} with AutoModelForCausalLM: {e}.")
                print("Retrying with AutoModel...")
                model_class = AutoModel
                force_download = False
            else:
                if has_tried_force_download:
                    raise e
                print(
                    f"Got error while loading model {base_model_name}: {e}.")
                print("Retrying with force_download=True...")
                model_class = AutoModelForCausalLM
                from_tf = False
                force_download = True
                has_tried_force_download = True

    tokenizer = get_tokenizer(base_model_name)

    if re.match("[^/]+/llama", base_model_name):
        model.config.pad_token_id = tokenizer.pad_token_id = 0
        model.config.bos_token_id = tokenizer.bos_token_id = 1
        model.config.eos_token_id = tokenizer.eos_token_id = 2

    loaded_models[base_model_name] = model
    return model

def clear_cache():
    gc.collect()

    torch = get_torch()
    # if not shared.args.cpu: # will not be running on CPUs anyway
    with torch.no_grad():
        torch.cuda.empty_cache()

def load_model(base_model_name:str,
        peft_model_name:str=None,data_dir:str="",load_8bit:bool=False):
    model_key = base_model_name
    if peft_model_name:
        model_key = f"{base_model_name}//{peft_model_name}"
    if model_key in loaded_models:
        return loaded_models[model_key]
    peft_model_name_or_path = peft_model_name
    if peft_model_name:
        lora_models_directory_path = os.path.join(
            data_dir, "lora_models")
        possible_lora_model_path = os.path.join(
            lora_models_directory_path, peft_model_name)
        if os.path.isdir(possible_lora_model_path):
            peft_model_name_or_path = possible_lora_model_path

            possible_model_info_json_path = os.path.join(
                possible_lora_model_path, "info.json")
            if os.path.isfile(possible_model_info_json_path):
                try:
                    with open(possible_model_info_json_path, "r") as file:
                        json_data = json.load(file)
                        possible_hf_model_name = json_data.get("hf_model_name")
                        if possible_hf_model_name and json_data.get("load_from_hf"):
                            peft_model_name_or_path = possible_hf_model_name
                except Exception as e:
                    raise ValueError(
                        "Error reading model info from {possible_model_info_json_path}: {e}")
    model = get_new_base_model(base_model_name)
    if peft_model_name:
        device = get_device()
        PeftModel = get_peft_model_class()

        if device == "cuda":
            model = PeftModel.from_pretrained(
                model,
                peft_model_name_or_path,
                torch_dtype=torch.float16,
                # ? https://github.com/tloen/alpaca-lora/issues/21
                device_map={'': 0}
            )
        else:
            model = PeftModel.from_pretrained(
                model,
                peft_model_name_or_path,
                device_map={"": device}
            )

    if re.match("[^/]+/llama", base_model_name):
        model.config.pad_token_id = get_tokenizer(
            base_model_name).pad_token_id = 0
        model.config.bos_token_id = 1
        model.config.eos_token_id = 2
    if not load_8bit:
        model.half()
    if torch.__version__ >= "2" and sys.platform != "win32":
        model = torch.compile(model)
    loaded_models[model_key] = model
    clear_cache()
    return model

def generate(
    # model
    model,
    tokenizer,
    # input
    prompt,
    generation_config,
    max_new_tokens,
    stopping_criteria=[],
):
    device = get_device()

    inputs = tokenizer(prompt, return_tensors="pt")
    input_ids = inputs["input_ids"].to(device)
    tokens_count=len(input_ids[0])
    if tokens_count>MAX_TOKEN_SIZE:
        raise Exception(f"This model's maximum context length is {MAX_TOKEN_SIZE}, input contains {tokens_count} tokens.  Please reduce the length of the messages.")
    generate_params = {
        "input_ids": input_ids,
        "generation_config": generation_config,
        "return_dict_in_generate": True,
        "output_scores": True,
        "max_new_tokens": max_new_tokens,
        "stopping_criteria": transformers.StoppingCriteriaList() + stopping_criteria
    }

    skip_special_tokens = True

    if '/dolly' in tokenizer.name_or_path:
        # dolly has additional_special_tokens as ['### End', '### Instruction:', '### Response:'], skipping them will break the prompter's reply extraction.
        skip_special_tokens = False
        # Ensure generation stops once it generates "### End"
        end_key_token_id = tokenizer.encode("### End")
        end_key_token_id = end_key_token_id[0]  # 50277
        if isinstance(generate_params['generation_config'].eos_token_id, str):
            generate_params['generation_config'].eos_token_id = [generate_params['generation_config'].eos_token_id]
        elif not generate_params['generation_config'].eos_token_id:
            generate_params['generation_config'].eos_token_id = []
        generate_params['generation_config'].eos_token_id.append(end_key_token_id)
    
    with torch.no_grad():
        generation_output = model.generate(**generate_params)
    output = generation_output.sequences[0]
    decoded_output = tokenizer.decode(output, skip_special_tokens=skip_special_tokens)
    return decoded_output, output, True

BASE_MODEL="decapoda-research/llama-7b-hf"
LORA_MODEL="obsidian-notes-sau-3072-2023-05-24-10-54-41"
TEMPLATE={
  "description": "Template used by Alpaca-LoRA.",
  "prompt_input": "Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.\n\n### Instruction:\n{instruction}\n\n### Input:\n{input}\n\n### Response:\n",
  "prompt_no_input": "Below is an instruction that describes a task. Write a response that appropriately completes the request.\n\n### Instruction:\n{instruction}\n\n### Response:\n",
  "response_split": "### Response:"
}
SYSTEM_TAG="<|SYSTEM|>"
ASSISTANT_TAG="<|ASSISTANT|>"
USER_TAG="<|USER|>"

class LoRA(LLM_Base):
    def get_response(self,system,assistant,user):
        base_model=BASE_MODEL
        lora_model=LORA_MODEL
        data_dir_realpath = LLM_FOLDER

        instruction=f"{SYSTEM_TAG}{system}{ASSISTANT_TAG}{assistant}"
        input=f"{USER_TAG}{user}"
        prompt = TEMPLATE["prompt_input"].format(instruction=instruction, input=input)

        tokenizer = get_tokenizer(base_model)
        lora_model_path=f"{data_dir_realpath}"
        model=load_model(base_model,lora_model,lora_model_path,False)
        temperature=0.1
        top_p=0.75
        top_k=40
        num_beams=4
        repetition_penalty=1.2
        max_new_tokens=MAX_TOKEN_SIZE
        generation_config = GenerationConfig(
                temperature=float(temperature),
                top_p=top_p,
                top_k=top_k,
                repetition_penalty=repetition_penalty,
                num_beams=num_beams,
                do_sample=False,
            )
        try:
            decoded_output, output, completed = generate(model,tokenizer,prompt,generation_config,max_new_tokens)
        except Exception as e:
            print(e)
            if LLM_Base.detect_if_tokens_oversized(e):
                LLM_Base.save_chat_cache(model,system,assistant,user,{"on_tokens_oversized":str(e)})
                return self.instant.on_tokens_oversized(e,system,assistant,user)
            return None
        response=decoded_output.split(TEMPLATE["response_split"])[1].strip()
        return response
    pass