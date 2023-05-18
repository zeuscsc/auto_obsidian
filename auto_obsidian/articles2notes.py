import json
import re
import os

from .gpt import get_chat_response,GPT3_MODEL
from .yt2txt import extract_video_id

OBSIDIAN_FOLDER = "obsidian_notes"
NOTES_FOLDER = f"{OBSIDIAN_FOLDER}/markdown_notes"
NOTES_BACKUP_FOLDER = "notes_backup/markdown_notes"
ARTICLES_INDEXES_JSON_FILE_PATH="articles_indexes.json"

def get_notes_from_chat(article:dict):
    system="""You are a scholars that is taking markdown notes about some video with Wiki style, you would be giving some written scripts for the task.
And summarize each paragraph with a title.
Remember to keep the technology or algorithm name, very important.
Please write the notes in markdown format.
Here is an example:
### Definiation
A deadlock is a situation in which two computer programs sharing the same resource are effectively preventing each other from accessing the resource, resulting in both programs ceasing to function. 
The earliest computer operating systems ran only one program at a time.

### What it have to do with Relationsal Database ManagementSystem
In a database, a deadlock is an unwanted situation in which two or more transactions are waiting indefinitely for one another to give up locks. 
Deadlock is said to be one of the most feared complications in DBMS as it brings the whole system to a Halt. 
When you tries to insert or update data on database, sometime your record need to depend on the row record.  
"""
    assistant="#### "
    user=str(article["text"])
    if len(user.split())<50:
        return None
    response=get_chat_response(GPT3_MODEL,system,assistant,user)
    return response
def get_title_from_notes(article:str):
    system="""You are a scholars that is taking markdown notes about some video, you would be giving some written scripts for the task.
You have finished writing the notes, and you want to extract the title from the notes.
The title should only be the name of the technology or algorithm, no extra words needed.
Please write the notes in markdown format. And since the title will also be use as the file name, please make sure the title is a valid file name.
No special characters allowed for the title.  Make sure the title is within 10 words.
Here is an example:
## Hidden Markov Model
"""
    assistant="## "
    user=article
    if len(user.split())<10:
        return None
    response=get_chat_response(GPT3_MODEL,system,assistant,user)
    return response
def get_files_in_directory(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
def get_note_path(video_id:str,note_name:str):
    os.makedirs(f"{NOTES_FOLDER}/{note_name} - ({video_id})", exist_ok=True)
    return f"{NOTES_FOLDER}/{note_name} - ({video_id})/{note_name}.md"
def get_backup_note_path(video_id:str,note_name:str):
    os.makedirs(f"{NOTES_BACKUP_FOLDER}/{video_id}", exist_ok=True)
    return f"{NOTES_BACKUP_FOLDER}/{video_id}/{note_name}.md"
def extract_title_from_md(md:str):
    first_line = md.strip().split('\n', 1)[0]
    title_match = re.match(r'^# (.+)$', first_line)
    if title_match:
        return title_match.group(1)
    else:
        return None
def check_if_notes_done(article_index):
    if "note_name" in article_index and article_index["note_name"] is not None:
        file_name=article_index["note_name"]
        video_id=extract_video_id(article_index["url"])
        md_file_path=get_note_path(video_id,file_name)
        if os.path.isfile(md_file_path):
            with open(md_file_path, "r",encoding="utf8") as md_file:
                content=md_file.read()
                if article_index["url"] in content:
                    return True
    return False
def load_articles_indexes():
    articles_indexes_json_file_path = ARTICLES_INDEXES_JSON_FILE_PATH
    if os.path.isfile(articles_indexes_json_file_path):
        with open(articles_indexes_json_file_path, "r",encoding="utf8") as articles_indexes_json_file:
            articles_indexes_json_data = json.load(articles_indexes_json_file)
            return articles_indexes_json_data
    return None
def save_articles_indexes(articles_indexes_json_data):
    articles_indexes_json_file_path = ARTICLES_INDEXES_JSON_FILE_PATH
    with open(articles_indexes_json_file_path, "w",encoding="utf8") as articles_indexes_json_file:
        json.dump(articles_indexes_json_data, articles_indexes_json_file, indent=4,ensure_ascii=False)
def load_article(article_index):
    file_path=article_index["file_path"]
    with open(file_path, "r",encoding="utf8") as article_json_file:
        article_json_data = json.load(article_json_file)
        return dict(article_index,**article_json_data)
def is_valid_filename(filename):
    try:
        return not set(filename).intersection(r'<>:"/\|?*')
    except OSError:
        pass

    return False

def generate():
    articles_indexes = load_articles_indexes()
    for key in articles_indexes:
        article_index=articles_indexes[key]
        if check_if_notes_done(article_index):
            continue
        article_title=str(article_index["title"])
        print(f"Generating: {article_title}...")
        article = load_article(article_index)
        url=article["url"]
        md_note_content=get_notes_from_chat(article)
        if md_note_content is None:
            continue
        title=get_title_from_notes(md_note_content)
        if title is None:
            continue
        obsidian_title=article_title.replace("[","").replace("]","")
        md_note=f"# {title}\n{md_note_content}"
        md_note+="\n\n"
        md_note+=f"Source: [{obsidian_title}]({url})\n"
        file_name=title.replace("# ","")
        if is_valid_filename(file_name):
            video_id=extract_video_id(url)
            md_file_path=get_note_path(video_id,file_name)
            md_backup_file_path=get_backup_note_path(video_id,file_name)
            # if os.path.isfile(md_file_path):
            #     print(f"Appending: {md_file_path}...")
            #     with open(md_file_path, "a",encoding="utf8") as md_file:
            #         md_file.write(md_note)
            # else:
            print(f"Saving: {md_file_path}...")
            with open(md_file_path, "w",encoding="utf8") as md_file:
                md_file.write(md_note)
            # with open(md_backup_file_path, "w",encoding="utf8") as md_file:
            #     md_file.write(md_note)
            article_index["note_name"]=file_name
            articles_indexes[key]=article_index
            save_articles_indexes(articles_indexes)
        else:
            print(f"Invalid file name: {file_name}")

if __name__ == "__main__":
    generate()