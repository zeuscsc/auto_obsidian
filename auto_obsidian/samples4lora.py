from .articles2notes import load_articles_indexes,load_article,ARTICLES2NOTE_INSTRUCTION,NOTE2TITLE_INSTRUCTION,article2note,note2title
from .folders import DATASETS_FOLDER

import os
import json
import hashlib

DATA_SOURCE="gpt4"

def calculate_md5(string:str):
    md5_hash = hashlib.md5(string.encode()).hexdigest()
    return md5_hash
def get_calls_stack_from_article(article:dict):
    from llm_picker.llm import LLM
    from llm_picker.cache import Cache
    from llm_picker.gpt import GPT,GPT4_MODEL
    llm4notes=LLM(Cache,save_call_history=True)
    # llm4notes=LLM(GPT,save_call_history=True)
    llm4notes.model_class.set_model_name(GPT4_MODEL)
    system=ARTICLES2NOTE_INSTRUCTION
    assistant="#### "
    user=str(article["text"])
    if len(user.split())<50:
        return None
    llm4notes.get_response(system,assistant,user)
    return llm4notes.get_called_history()
def get_calls_history_from_notes(article:str):
    from llm_picker.llm import LLM
    from llm_picker.cache import Cache
    from llm_picker.gpt import GPT,GPT4_MODEL
    llm4notes=LLM(Cache,save_call_history=True)
    # llm4notes=LLM(GPT,save_call_history=True)
    llm4notes.model_class.set_model_name(GPT4_MODEL)
    system=NOTE2TITLE_INSTRUCTION
    assistant="## "
    user=article
    if len(user.split())<10:
        return None
    response=llm4notes.get_response(system,assistant,user)
    response=str(response).replace(":"," - ")
    llm4notes.get_response(system,assistant,user)
    return llm4notes.get_called_history()


def get_notes_from_article(article:dict):
    from llm_picker.llm import LLM
    from llm_picker.cache import Cache
    from llm_picker.gpt import GPT4_MODEL
    llm4notes=LLM(Cache)
    llm4notes.model_class.set_model_name(GPT4_MODEL)
    system=ARTICLES2NOTE_INSTRUCTION
    assistant="#### "
    user=str(article["text"])
    if len(user.split())<50:
        return None
    response=llm4notes.get_response(system,assistant,user)
    return response
def get_title_from_notes(article:str):
    system=NOTE2TITLE_INSTRUCTION
    assistant="## "
    user=article
    response=note2title(article)
    return system,assistant,user,str(response).replace(":"," - ")
def generate():
    articles_indexes = load_articles_indexes()
    training_dataset=[]
    md5_hashes=[]
    for key in articles_indexes:
        article_index=articles_indexes[key]
        os.makedirs(f"{DATASETS_FOLDER}/{DATA_SOURCE}",exist_ok=True)
        article_title=str(article_index["title"])
        print(f"Generating: {article_title}...")
        article = load_article(article_index)
        if article is None:
            continue

        # system,assistant,user,md_note_content=get_notes_from_chat(article)
        responses_calls_stack=get_calls_stack_from_article(article)
        if responses_calls_stack is not None:
            for stack in responses_calls_stack:
                if stack is None:
                    print("Stack is None")
                    continue
                system=stack.system
                assistant=stack.assistant
                user=stack.user
                md_note_content=stack.response
                if md_note_content is not None:
                    instruction=f"<|SYSTEM|>{system}<|ASSISTANT|>{assistant}"
                    input=f"<|USER|>{user}"
                    output=f"{md_note_content}"
                    md5_hashed=calculate_md5(f"{instruction}{input}{output}")
                    if md5_hashed not in md5_hashes:
                        md5_hashes.append(md5_hashed)
                        training_dataset.append({"instruction":instruction,"input":input,"output":output})
        md_note_content=get_notes_from_article(article)
        if md_note_content is not None:
            responses_calls_stack=get_calls_history_from_notes(md_note_content)
            if responses_calls_stack is not None:
                for stack in responses_calls_stack:
                    if stack is None:
                        print("Stack is None")
                        continue
                    system=stack.system
                    assistant=stack.assistant
                    user=stack.user
                    title=stack.response
                    if title is not None and title!="None":
                        instruction=f"<|SYSTEM|>{system}<|ASSISTANT|>{assistant}"
                        input=f"<|USER|>{user}"
                        output=f"{title}"
                        md5_hashed=calculate_md5(f"{instruction}{input}{output}")
                        if md5_hashed not in md5_hashes:
                            md5_hashes.append(md5_hashed)
                            training_dataset.append({"instruction":instruction,"input":input,"output":output})

    print("Saving...")
    with open(f"{DATASETS_FOLDER}/{DATA_SOURCE}/auto_obsidian.json", "w",encoding="utf8") as training_dataset_json_file:
        json.dump(training_dataset, training_dataset_json_file, indent=4,ensure_ascii=False)

if __name__ == "__main__":
    generate()