from .articles2notes import get_note_path,load_articles_indexes,load_article,save_articles_indexes
from .snapshots4notes import load_note,save_note
from .ytdl import extract_video_id

import re

try_counter=0
def remove_brackets(text):
    if text.count('[') > 0 and text.count(']') > 0:
        start = text.index('[')
        end = text.rindex(']') + 1 
        return text[:start] + text[end:]
    else:
        return text
def collapse_brackets(text):
    while re.search(r'\[\[.*\|.*\]\]', text):
        text = re.sub(r'\[\[(.*)\|.*\]\]', r'[\1]', text)
    return text
def is_mentioned(text:str, mention:str):
    mention = mention.lower()
    text = text.lower()
    text_without_brackets = remove_brackets(text)
    pattern = r'\b' + re.escape(mention) + r'\b'
    return bool(re.search(pattern, text_without_brackets))
def auto_link_mentions(text:str, mentions:list[str],exclude_mentions:list[str]=[]):
    mentions=list(mentions)
    mentions.sort(key=len, reverse=True)
    # text=collapse_brackets(text)
    mentions_linked=[]
    for mention in mentions:
        if mention.lower() in exclude_mentions or mention.lower() in mentions_linked:
            # print(mention)
            continue
        if is_mentioned(text,mention):
            mentions_linked.append(mention.lower())
            start_index = text.lower().find(mention.lower())
            end_index=start_index+len(mention)
            text=text[:start_index]+f'[[{mention}|{text[start_index:end_index]}]]'+text[end_index:]
    return text

def link_all_notes():
    articles_indexes=load_articles_indexes()
    notes_map=dict()
    articles_notes_map=dict()
    for key in articles_indexes:
        article_index=articles_indexes[key]
        video_id=extract_video_id(article_index["url"])
        if "note_name" in article_index:
            note_name=str(article_index["note_name"])
            note=load_note(video_id,note_name)
            notes_map[note_name.lower()]=note
            articles_notes_map[note_name.lower()]=article_index
    for key in notes_map:
        note=str(notes_map[key])
        article_index=articles_notes_map[key]
        video_id=extract_video_id(article_index["url"])
        senstances=note.split("\n")
        linked_note=""
        for sentence in senstances:
            linked_note+=auto_link_mentions(sentence,notes_map.keys(),[str(key).lower()])+"\n"
        save_note(video_id,key,linked_note)
    return

