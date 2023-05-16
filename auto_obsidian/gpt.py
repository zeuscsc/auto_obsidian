import openai
from dotenv import load_dotenv
import os
import json
import datetime
from time import sleep
import re

load_dotenv()

GPT3_MODEL = "gpt-3.5-turbo"
GPT4_MODEL = "gpt-4"
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
TECKY_API_KEY = os.getenv('TECKY_API_KEY')
TEMP_FOLDER = "./temp"

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

def switch2tecky():
    openai.api_key = TECKY_API_KEY
    openai.api_base = "https://api.gpt.tecky.ai/v1"
def switch2openai():
    openai.api_key = OPENAI_API_KEY
    openai.api_base = "https://api.openai.com/v1"
def get_chat_response(model,system,assistant,user):
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
        now = datetime.datetime.now()
        time_string = now.strftime("%Y%m%d%H%M%S")
        os.makedirs(TEMP_FOLDER, exist_ok=True)
        with open(f"{TEMP_FOLDER}/{time_string}.json", "w",encoding="utf8") as temp_file:
            json.dump(completion, temp_file, indent=4, ensure_ascii=False)
        return completion.choices[0].message.content
    except Exception as e:
        print(e)
        if re.search(r"This model's maximum context length is", str(e)) is not None and \
            re.search(r"tokens", str(e)) is not None and \
            re.search(r"Please reduce the length of the messages.", str(e)) is not None:
            print("Splitting text in half...")
            chunks = []
            chunks.extend(split_text_in_half(user))
            responses=""
            for chunk in chunks:
                responses+=get_chat_response(model,system,assistant,chunk)
            return responses
        else:
            global gpt_error_delay
            sleep(gpt_error_delay)
            gpt_error_delay=gpt_error_delay*2
            return get_chat_response(model,system,assistant,user)
def get_chats_responses(model,system,assistant,user):
    chunks = []
    chunks.extend(split_text_in_half_if_too_large(user))
    responses=""
    for chunk in chunks:
        assistant+=responses
        responses=get_chat_response(model,system,assistant,chunk)
    return responses