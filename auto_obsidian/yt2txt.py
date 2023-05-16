import json
import os
import subprocess
import whisper
import torch
import glob
import json

from ytdl import extract_video_id, download,VIDEOS_FOLDER

AUDIO_FOLDER = "audios"
ARTICLES_FOLDER = "articles"
class SiteCard:
    title:str
    url:str
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    pass
def get_all_toby_files():
    matching_files = glob.glob(f"toby_export_json_files/toby-export-*.json")
    return matching_files
def get_sites_cards()->list[SiteCard]:
    toby_files_paths=get_all_toby_files()
    sites_cards=[]
    for toby_file_path in toby_files_paths:
        with open(toby_file_path, "r",encoding="utf8") as json_file:
            json_data = json.load(json_file)
            lists = json_data["lists"]
            for list in lists:
                cards = list["cards"]
                for card in cards:
                    sites_cards.append(SiteCard(**card))
    print(f"Loaded {len(sites_cards)} sites cards")
    return sites_cards
def download_youtube_videos(cards:list[SiteCard]):
    print(f"Downloading {len(cards)} youtube videos...")
    for card in cards:
        url=card.url
        video_id = extract_video_id(url)
        if video_id is not None:
            download(video_id)
    pass
def get_audio_path(filename:str):
    return f"{AUDIO_FOLDER}/{filename}.m4a"
def extract_audios():
    files = os.listdir(VIDEOS_FOLDER)
    os.makedirs(AUDIO_FOLDER, exist_ok=True)
    for file in files:
        filename, file_extension = os.path.splitext(file)
        if os.path.exists(get_audio_path(filename)):
            print(f"Skipping {file} because it already exists")
            continue
        command=f"ffmpeg -i {VIDEOS_FOLDER}/{file} -vn -c:a aac -b:a 128k -y {get_audio_path(filename)}"
        subprocess.call(command, shell=True)
    pass
def speech2text(cards:list[SiteCard]):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = whisper.load_model("medium.en").to(device)
    articles_indexes=dict()
    for card in cards:
        title=card.title
        url=card.url
        video_id = extract_video_id(url)
        if video_id is not None:
            file_path=f"{ARTICLES_FOLDER}/{video_id}.json"
            if os.path.exists(file_path):
                print(f"Skipping {file_path} because it already exists")
                continue
            print(f"Transcribing: {title}...")
            result = model.transcribe(get_audio_path(video_id))
            article_index={"title":title,"url":url,"file_path":file_path}
            articles_indexes[video_id]=article_index
            article = dict(article_index, **result)
            with open(file_path, "w",encoding="utf8") as json_file:
                json.dump(article, json_file, indent=4)
            with open("articles_indexes.json", "w",encoding="utf8") as json_file:
                json.dump(articles_indexes, json_file, indent=4)
    pass
if __name__ == "__main__":
    sites_cards=get_sites_cards()
    download_youtube_videos(sites_cards)
    extract_audios()
    speech2text(sites_cards)