from sentence_transformers import SentenceTransformer
import os
from scipy import spatial

from .folders import SNAPSHOTS_FOLDER,NOTES_WITH_SNAPSHOT_CACHE_FOLDER,NOTES_FOLDER
from .ytdl import extract_video_id
from .video2snapshots import save_snapshot,load_video,unload_video,get_relative_image_path
from .articles2notes import get_note_path,load_articles_indexes,load_article,save_articles_indexes

def initialize():
    load_model()

def load_model():
    global model
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
def get_notes_with_snapshot_cache_path(video_id,note_name):
    from .llm import get_best_available_llm
    model_name=get_best_available_llm().get_model_name()
    note_path=get_note_path(video_id,note_name)
    note_path=note_path.replace(NOTES_FOLDER,f"{NOTES_WITH_SNAPSHOT_CACHE_FOLDER}\{model_name}")
    return note_path
def load_note(video_id,note_name):
    note_path=get_note_path(video_id,note_name)
    with open(note_path, "r",encoding="utf8") as note_file:
        note=note_file.read()
        return note
def save_note(video_id,note_name,note):
    note_path=get_note_path(video_id,note_name)
    os.makedirs(os.path.dirname(note_path), exist_ok=True)
    with open(note_path, "w",encoding="utf8") as note_file:
        note_file.write(note)
def load_notes_with_snapshot_cache(video_id,note_name):
    note_path=get_notes_with_snapshot_cache_path(video_id,note_name)
    if os.path.exists(note_path)==False:
        return None
    print(f"Loading note with snapshot cache {note_path}")
    with open(note_path, "r",encoding="utf8") as note_file:
        note=note_file.read()
        return note
def save_notes_with_snapshot_cache(video_id,note_name,note):
    note_path=get_notes_with_snapshot_cache_path(video_id,note_name)
    os.makedirs(os.path.dirname(note_path), exist_ok=True)
    with open(note_path, "w",encoding="utf8") as note_file:
        note_file.write(note)

def get_sentence_embedding(sentences:list[str]):
    return model.encode(sentences)
def add_snapshot4notes_with_speeches():
    os.makedirs(SNAPSHOTS_FOLDER, exist_ok=True)
    articles_indexes=load_articles_indexes()
    for key in articles_indexes:
        article_index=articles_indexes[key]
        video_id=extract_video_id(article_index["url"])
        load_video(video_id)
        article=load_article(article_index)
        if article is None:
            continue
        article_sentences=[]
        segments=article["segments"]
        for segment in segments:
            article_sentences.append(segment["text"])
        if "note_name" in article_index:
            note_name=article_index["note_name"]
            note=load_notes_with_snapshot_cache(video_id,note_name)
            if note is None:
                note=load_note(video_id,note_name)
                note_subtitles=[]
                print(f"Extracting snapshots for {note_name}")
                note_sentences=note.split("\n")
                for note_sentence in note_sentences:
                    if note_sentence!="" and note_sentence.startswith("Source: ")==False and len(note_sentence.split())>5:
                        snapshot_index=len(note_subtitles)
                        note_subtitles.append(note_sentence)
                        note=note.replace(f"{note_sentence}",f"{note_sentence} ![[snapshot_{snapshot_index}]]")
                senstances=note_subtitles+article_sentences
                embeddings=get_sentence_embedding(senstances)
                for note_index in range(len(note_subtitles)):
                    note_sentence=note_subtitles[note_index]
                    note_subtitle_embedding=embeddings[note_index]
                    similarities=[]
                    for article_sentences_index in range(len(article_sentences)):
                        article_sentence_embedding=embeddings[article_sentences_index+len(note_subtitles)]
                        similarity=1-spatial.distance.cosine(note_subtitle_embedding, article_sentence_embedding)
                        similarities.append(similarity)
                    max_similarity=max(similarities)
                    max_similarity_index=similarities.index(max_similarity)
                    start=article["segments"][max_similarity_index]["start"]
                    end=article["segments"][max_similarity_index]["end"]
                    snapshot_index=note_index
                    try:
                        snapshot_time,snapshot_file_path=save_snapshot(video_id,start,end)
                        if snapshot_file_path is not None:
                            relative_image_path=get_relative_image_path(snapshot_file_path)
                            if f"![[{relative_image_path}]]" not in note:
                                note=note.replace(f"![[snapshot_{snapshot_index}]]",f"[![[{relative_image_path}]]](<https://youtu.be/{video_id}?t={int(snapshot_time)}s>)")
                            else:
                                note=note.replace(f"![[snapshot_{snapshot_index}]]","")
                        else:
                            note=note.replace(f"![[snapshot_{snapshot_index}]]","")
                    except Exception as e:
                        print(e)
                        note=note.replace(f"![[snapshot_{snapshot_index}]]","")
                save_notes_with_snapshot_cache(video_id,note_name,note)  
            save_note(video_id,note_name,note)
        unload_video()
        pass

if __name__ == "__main__":
    initialize()
    add_snapshot4notes_with_speeches()