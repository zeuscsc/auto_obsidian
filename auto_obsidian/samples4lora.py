from .articles2notes import load_articles_indexes,load_article,ARTICLES2NOTE_INSTRUCTION,NOTE2TITLE_INSTRUCTION,article2note,note2title
from .folders import DATASETS_FOLDER

import os
import json

DATA_SOURCE="gpt4"

def get_notes_from_chat(article:dict):
    system=ARTICLES2NOTE_INSTRUCTION
    assistant="#### "
    user=str(article["text"])
    response=article2note(article)
    return system,assistant,user,response
def get_title_from_notes(article:str):
    system=NOTE2TITLE_INSTRUCTION
    assistant="## "
    user=article
    response=note2title(article)
    return system,assistant,user,str(response).replace(":"," - ")
def generate():
    articles_indexes = load_articles_indexes()
    training_dataset=[]
    for key in articles_indexes:
        article_index=articles_indexes[key]
        os.makedirs(f"{DATASETS_FOLDER}/{DATA_SOURCE}",exist_ok=True)
        article_title=str(article_index["title"])
        print(f"Generating: {article_title}...")
        article = load_article(article_index)
        if article is None:
            continue

        system,assistant,user,md_note_content=get_notes_from_chat(article)
        if md_note_content is not None:
            instruction=f"<|SYSTEM|>{system}<|ASSISTANT|>{assistant}"
            input=f"<|USER|>{user}"
            output=f"{md_note_content}"
            training_dataset.append({"instruction":instruction,"input":input,"output":output})
            system,assistant,user,title=get_title_from_notes(md_note_content)
            instruction=f"<|SYSTEM|>{system}<|ASSISTANT|>{assistant}"
            input=f"<|USER|>{user}"
            output=f"{title}"
            training_dataset.append({"instruction":instruction,"input":input,"output":output})

    print("Saving...")
    with open(f"{DATASETS_FOLDER}/{DATA_SOURCE}/auto_obsidian.json", "w",encoding="utf8") as training_dataset_json_file:
        json.dump(training_dataset, training_dataset_json_file, indent=4,ensure_ascii=False)

if __name__ == "__main__":
    generate()