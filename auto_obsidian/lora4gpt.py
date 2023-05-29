import torch
from transformers import (
    AutoModelForCausalLM, AutoModel,
    AutoTokenizer, LlamaTokenizer
)
import re
import os
import json
import gc
import peft
import sys

loaded_models = dict()
loaded_tokenizers = dict()

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
            trust_remote_code=True
        )
    else:
        return model_class.from_pretrained(
            model_name,
            device_map={"": device},
            low_cpu_mem_usage=True,
            from_tf=from_tf,
            force_download=force_download,
            trust_remote_code=True
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
        if 'LLaMATokenizer' in str(e):
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
        peft_model_name:str=None,data_dir:str=""):
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
        elif device == "mps":
            model = PeftModel.from_pretrained(
                model,
                peft_model_name_or_path,
                device_map={"": device},
                torch_dtype=torch.float16
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
    if torch.__version__ >= "2" and sys.platform != "win32":
        model = torch.compile(model)
    loaded_models[model_key] = model
    clear_cache()
    return model

