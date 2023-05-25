import openai
import os
import json
import datetime
from time import sleep
import re
import hashlib
import glob

from .folders import CHAT_CACHE_FOLDER

GPT3_MODEL = "gpt-3.5-turbo"
GPT4_MODEL = "gpt-4"
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
TECKY_API_KEY = os.environ.get('TECKY_API_KEY')

gpt_error_delay=2

def split_text_in_half_if_too_large(text,max_tokens=10000):
    words = text.split()
    results = []
    
    if len(words) <= max_tokens:
        results.append(' '.join(words))
    else:
        half = len(words) // 2
        results.extend(split_text_in_half_if_too_large(' '.join(words[:half])))
        results.extend(split_text_in_half_if_too_large(' '.join(words[half:])))
    return results
def split_text_in_half(text):
    words = text.split()
    results = []
    half = len(words) // 2
    results.extend(split_text_in_half_if_too_large(' '.join(words[:half])))
    results.extend(split_text_in_half_if_too_large(' '.join(words[half:])))
    return results

def calculate_md5(string:str):
    md5_hash = hashlib.md5(string.encode()).hexdigest()
    return md5_hash
def switch2tecky():
    openai.api_key = TECKY_API_KEY
    openai.api_base = "https://api.gpt.tecky.ai/v1"
def switch2openai():
    openai.api_key = OPENAI_API_KEY
    openai.api_base = "https://api.openai.com/v1"

def load_chat_cache(model,system,assistant,user):
    try:
        hashed_request=calculate_md5(f"{model}{system}{assistant}{user}")
        matching_files = glob.glob(f"{CHAT_CACHE_FOLDER}/{hashed_request}/*.json")
        if len(matching_files)>0:
            with open(matching_files[-1], "r",encoding="utf8") as chat_cache_file:
                chat_cache = json.load(chat_cache_file)
                return chat_cache
    except Exception as e:
        print(e)
    return None
def save_chat_cache(model,system,assistant,user,chat_cache):
    hashed_request=calculate_md5(f"{model}{system}{assistant}{user}")
    now = datetime.datetime.now()
    time_string = now.strftime("%Y%m%d%H%M%S")
    os.makedirs(f"{CHAT_CACHE_FOLDER}/{hashed_request}", exist_ok=True)
    with open(f"{CHAT_CACHE_FOLDER}/{hashed_request}/{time_string}.json", "w",encoding="utf8") as temp_file:
        json.dump(chat_cache, temp_file, indent=4, ensure_ascii=False)
def delete_chat_cache(model,system,assistant,user):
    hashed_request=calculate_md5(f"{model}{system}{assistant}{user}")
    matching_files = glob.glob(f"{CHAT_CACHE_FOLDER}/{hashed_request}/*.json")
    for file in matching_files:
        os.remove(file)
def detect_if_tokens_oversized(e):
    return re.search(r"This model's maximum context length is", str(e)) is not None and \
        re.search(r"tokens", str(e)) is not None and \
        re.search(r"Please reduce the length of the messages.", str(e)) is not None or \
        (re.search(r"HTTP code 413 from API", str(e)) is not None and \
            re.search(r"PayloadTooLargeError: request entity too large", str(e)) is not None)
def on_tokens_oversized(e,model,system,assistant,user):
    if detect_if_tokens_oversized(e):
        print("Splitting text in half...")
        chunks = []
        chunks.extend(split_text_in_half(user))
        responses=""
        for chunk in chunks:
            responses+=get_chat_response(model,system,assistant,chunk)
            return responses
def get_chat_response(model,system,assistant,user):
    chat_cache=load_chat_cache(model,system,assistant,user)
    if chat_cache is not None:
        if "choices" in chat_cache and len(chat_cache["choices"])>0 and "message" in chat_cache["choices"][0] and \
            "content" in chat_cache["choices"][0]["message"]:
            return chat_cache["choices"][0]["message"]["content"]
        elif "on_tokens_oversized" in chat_cache:
            e=chat_cache["on_tokens_oversized"]
            return on_tokens_oversized(e,model,system,assistant,user)
        elif "choices" in chat_cache and len(chat_cache["choices"])>0 and "message" in chat_cache["choices"][0] and \
            "content" not in chat_cache["choices"][0]["message"]:
            delete_chat_cache(model,system,assistant,user)
    if model=="gpt-3.5-turbo":
        switch2openai()
    elif model=="gpt-4":
        switch2tecky()
    print(f"Connecting to {model} model...")
    try:
        completion = openai.ChatCompletion.create(
            model=model,
            messages=[
                    {"role": "system","content": system},
                    {"role": "assistant","content": assistant},
                    {"role": "user","content": user}
                ],
            )
        save_chat_cache(model,system,assistant,user,completion)
        return completion.choices[0].message.content
    except Exception as e:
        print(e)
        if detect_if_tokens_oversized(e):
            save_chat_cache(model,system,assistant,user,{"on_tokens_oversized":str(e)})
            return on_tokens_oversized(e,model,system,assistant,user)
        else:
            global gpt_error_delay
            sleep(gpt_error_delay)
            gpt_error_delay=gpt_error_delay*2
            return get_chat_response(model,system,assistant,user)
