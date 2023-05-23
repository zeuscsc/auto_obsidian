from .articles2notes import get_note_path,load_articles_indexes,load_article,save_articles_indexes
from .snapshots4notes import load_note,save_note
from .ytdl import extract_video_id

import re

try_counter=0
plural_adder=None

def remove_brackets(text:str):
    if text.count('[') > 0 and text.count(']') > 0:
        start = text.index('[')
        end = text.rindex(']') + 1 
        return text[:start] + text[end:]
    else:
        return text
def is_mentioned(text:str, mention:str):
    mention = mention.lower()
    text = text.lower()
    text_without_brackets = remove_brackets(text)
    pattern = r'\b' + re.escape(mention) + r'\b'
    return bool(re.search(pattern, text_without_brackets))
def find_mentions(text, mention):
    pattern = r'(?<!\[){}(?!\])'.format(re.escape(mention))
    matches = re.finditer(pattern, text)
    indexes = [match.start() for match in matches]
    return indexes
def auto_link_mentions(text:str, mentions:list[str],exclude_mentions:list[str]=[]):
    global plural_adder
    if plural_adder is None:
        import inflect
        plural_adder = inflect.engine()
    mentions=list(mentions)
    mentions.sort(key=len, reverse=True)
    for mention in mentions:
        if mention.lower() in exclude_mentions:
            continue
        mention_with_plurals_versions:list[str]=[]
        mention_with_plurals_versions.append(plural_adder.plural_noun(mention,1))
        mention_with_plurals_versions.append(plural_adder.plural_noun(mention,2))
        for mention_version in mention_with_plurals_versions:
            start_index=text.lower().find(mention_version.lower())
            if start_index==-1:
                continue
            end_index=start_index+len(mention_version)
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
        print(f"Linking {key}")
        note=str(notes_map[key])
        article_index=articles_notes_map[key]
        video_id=extract_video_id(article_index["url"])
        senstances=note.split("\n")
        linked_note=""
        for sentence in senstances:
            if sentence.startswith("Source:") or sentence.startswith("#"):
                linked_note+=sentence+"\n"
                continue
            linked_note+=auto_link_mentions(sentence,notes_map.keys(),[str(key).lower()])+"\n"
        save_note(video_id,key,linked_note)
    return

