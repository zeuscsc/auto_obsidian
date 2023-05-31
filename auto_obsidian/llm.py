import os
import json
import datetime
import re
import hashlib
import glob
from abc import ABC, abstractmethod
from typing import Type
from .folders import LLM_RESPONSE_CACHE_FOLDER

def calculate_md5(string:str):
    md5_hash = hashlib.md5(string.encode()).hexdigest()
    return md5_hash

class _LLM_Base(ABC):
    def load_response_cache(model,system,assistant,user):
        try:
            hashed_request=calculate_md5(f"{model}{system}{assistant}{user}")
            matching_files = glob.glob(f"{LLM_RESPONSE_CACHE_FOLDER}/{hashed_request}/*.json")
            if len(matching_files)>0:
                with open(matching_files[-1], "r",encoding="utf8") as chat_cache_file:
                    chat_cache = json.load(chat_cache_file)
                    return chat_cache
        except Exception as e:
            print(e)
        return None
    def save_response_cache(model,system,assistant,user,chat_cache):
        hashed_request=calculate_md5(f"{model}{system}{assistant}{user}")
        now = datetime.datetime.now()
        time_string = now.strftime("%Y%m%d%H%M%S")
        os.makedirs(f"{LLM_RESPONSE_CACHE_FOLDER}/{hashed_request}", exist_ok=True)
        with open(f"{LLM_RESPONSE_CACHE_FOLDER}/{hashed_request}/{time_string}.json", "w",encoding="utf8") as temp_file:
            json.dump(chat_cache, temp_file, indent=4, ensure_ascii=False)
    def delete_response_cache(model,system,assistant,user):
        hashed_request=calculate_md5(f"{model}{system}{assistant}{user}")
        matching_files = glob.glob(f"{LLM_RESPONSE_CACHE_FOLDER}/{hashed_request}/*.json")
        for file in matching_files:
            os.remove(file)
    def detect_if_tokens_oversized(e):
        return re.search(r"This model's maximum context length is", str(e)) is not None and \
            re.search(r"tokens", str(e)) is not None and \
            re.search(r"Please reduce the length of the messages.", str(e)) is not None or \
            (re.search(r"HTTP code 413 from API", str(e)) is not None and \
                re.search(r"PayloadTooLargeError: request entity too large", str(e)) is not None)
    def detect_if_result_filtered(e):
        return re.search(r"The response was filtered due to the prompt triggering Azure OpenAI’s content management policy.", str(e)) is not None
    def split_text_in_half_if_too_large(text:str,max_tokens=10000):
        words = text.split()
        results = []
        
        if len(words) <= max_tokens:
            results.append(' '.join(words))
        else:
            half = len(words) // 2
            results.extend(_LLM_Base.split_text_in_half_if_too_large(' '.join(words[:half])))
            results.extend(_LLM_Base.split_text_in_half_if_too_large(' '.join(words[half:])))
        return results
    def split_text_in_half(text:str):
        words = text.split()
        results = []
        half = len(words) // 2
        results.extend(_LLM_Base.split_text_in_half_if_too_large(' '.join(words[:half])))
        results.extend(_LLM_Base.split_text_in_half_if_too_large(' '.join(words[half:])))
        return results

    @abstractmethod
    def get_response(self,system,assistant,user):
        pass

    def on_tokens_oversized(self,e,system,assistant,user):
        if _LLM_Base.detect_if_tokens_oversized(e):
            print("Splitting text in half...")
            chunks = []
            chunks.extend(_LLM_Base.split_text_in_half(user))
            responses=""
            for chunk in chunks:
                response=self.get_response(system,assistant,chunk)
                if response is not None:
                    responses+=response
                return responses
    
    pass


class LLM_Base(_LLM_Base):
    def __init__(self,instant:_LLM_Base) -> None:
        self.instant=instant
        pass
    pass

class LLM:
    def __init__(self,ModelClass:Type[LLM_Base]) -> None:
        self.model_class=ModelClass(self)
        pass
    def get_response(self,system,assistant,user):
        return self.model_class.get_response(system,assistant,user)
    def on_tokens_oversized(self,e,system,assistant,user):
        return self.model_class.on_tokens_oversized(e,system,assistant,user)
    pass

def get_best_available_llm():
    from .gpt import GPT
    model=GPT.model_picker()
    if model is not None:
        print(f"Using {model} model")
        instant=LLM(GPT)
    else:
        print(f"Failed to connect to OpenAi, using LoRA model instead.")
        from .lora import LoRA
        instant=LLM(LoRA)
    return instant