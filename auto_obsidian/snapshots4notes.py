from sentence_transformers import SentenceTransformer
import os
from video2snapshots import SNAPSHOTS_FOLDER,extract_snapshot,load_video,unload_video,get_snapshot_time,get_snapshot_path
from articles2notes import get_note_path,load_articles_indexes,load_article,save_articles_indexes
from scipy import spatial
from ytdl import extract_video_id

def initialize():
    load_model()

def load_model():
    global model
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
def load_note(video_id,note_name):
    note_path=get_note_path(video_id,note_name)
    with open(note_path, "r",encoding="utf8") as note_file:
        note=note_file.read()
        return note
def save_note(video_id,note_name,note):
    note_path=get_note_path(video_id,note_name)
    with open(note_path, "w",encoding="utf8") as note_file:
        note_file.write(note)

def get_sentence_embedding(sentences:list[str]):
    return model.encode(sentences)
def match_notes_with_speeches():
    os.makedirs(SNAPSHOTS_FOLDER, exist_ok=True)
    articles_indexes=load_articles_indexes()
    for key in articles_indexes:
        article_index=articles_indexes[key]
        video_id=extract_video_id(article_index["url"])
        load_video(video_id)
        article=load_article(article_index)
        article_sentences=[]
        segments=article["segments"]
        for segment in segments:
            article_sentences.append(segment["text"])
        note_name=article_index["note_name"]
        note=load_note(video_id,note_name)
        note_subtitles=[]
        print(f"Extracting snapshots for {note_name}")
        note_sentences=note.split("\n")
        for note_sentence in note_sentences:
            if note_sentence!="" and note_sentence.startswith("Source: ")==False:
                snapshot_index=len(note_subtitles)
                note_subtitles.append(note_sentence)
                note=note.replace(f"{note_sentence}",f"![[snapshot_{snapshot_index}]]{note_sentence}")
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
            snapshot_time=get_snapshot_time(start,end)
            snapshot_file_path=get_snapshot_path(video_id,snapshot_time)
            snapshot_index=note_index
            if os.path.exists(snapshot_file_path):
                note=note.replace(f"![[snapshot_{snapshot_index}]]","")
            else:
                snapshot_file_path=extract_snapshot(video_id,start,end)
                note=note.replace(f"![[snapshot_{snapshot_index}]]",f"![[{snapshot_file_path}]]\n")
        save_note(video_id,note_name,note)
        unload_video()
        article_index["done"]=True
        save_articles_indexes(articles_indexes)
        pass

if __name__ == "__main__":
    initialize()
    match_notes_with_speeches()