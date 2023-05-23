import json
import os
import subprocess
import torch
import glob
import json

from .folders import VIDEOS_FOLDER,ARTICLES_FOLDER,AUDIO_FOLDER
from .ytdl import extract_video_id, download

LARGE_WHISPER_MODEL_NAME="large"
MEDIUM_WHISPER_MODEL_NAME="medium.en"

model=None

import pynvml

def get_gpu_vram():
    """Get information about GPU vRAM."""
    try:
        # Initialize NVML
        pynvml.nvmlInit()

        # Get the number of GPUs
        device_count = pynvml.nvmlDeviceGetCount()

        if device_count > 0:
            # Get the handle of the first GPU
            handle = pynvml.nvmlDeviceGetHandleByIndex(0)

            # Get the memory info
            mem_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
            total_vram = mem_info.total
            used_vram = mem_info.used
            free_vram = mem_info.free

            # Print or return the information as desired
            print(f"Total GPU vRAM: {total_vram} bytes")
            print(f"Used GPU vRAM: {used_vram} bytes")
            print(f"Free GPU vRAM: {free_vram} bytes")

            # Return the information as a dictionary if needed
            return {
                "total_vram": total_vram,
                "used_vram": used_vram,
                "free_vram": free_vram
            }
        else:
            print("No GPU found.")
            return None

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Clean up NVML
        pynvml.nvmlShutdown()

def convert_to_bytes(size):
    """Convert a string representing a size to bytes."""
    multipliers = {
        'B': 1,
        'KB': 1024,
        'MB': 1024 ** 2,
        'GB': 1024 ** 3,
        'TB': 1024 ** 4,
        'PB': 1024 ** 5
    }
    number, unit = size[:-2], size[-2:].strip().upper()

    try:
        bytes_value = int(float(number) * multipliers[unit])
        return bytes_value
    except (ValueError, KeyError):
        raise ValueError("Invalid size format.")
def load_model():
    global model
    if model is None:
        import whisper
        device = "cuda" if torch.cuda.is_available() else "cpu"
        vRamInfo=get_gpu_vram()
        if vRamInfo["free_vram"]>convert_to_bytes("10GB"):
            model = whisper.load_model(LARGE_WHISPER_MODEL_NAME).to(device)
        elif vRamInfo["free_vram"]>convert_to_bytes("5GB"):
            print("Failed to load large model, fallback to loading medium model...")
            model=whisper.load_model(MEDIUM_WHISPER_MODEL_NAME).to(device)
    return model
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
    from .articles2notes import save_articles_indexes,load_articles_indexes
    articles_indexes=load_articles_indexes()
    if articles_indexes is None:
        articles_indexes=dict()
    for card in cards:
        title=card.title
        url=card.url
        video_id = extract_video_id(url)
        if video_id is not None:
            file_path=f"{ARTICLES_FOLDER}/{video_id}.json"
            if video_id not in articles_indexes:
                article_index={"title":title,"url":url,"file_path":file_path}
                articles_indexes[video_id]=article_index
                save_articles_indexes(articles_indexes)
            else:
                article_index=articles_indexes[video_id]
            if os.path.exists(file_path):
                print(f"Skipping {file_path} because it already exists")
                continue
            model=load_model()
            print(f"Transcribing: {title}...")
            result = model.transcribe(get_audio_path(video_id))
            article = dict(article_index, **result)
            with open(file_path, "w",encoding="utf8") as json_file:
                json.dump(article, json_file, indent=4)
    pass
if __name__ == "__main__":
    sites_cards=get_sites_cards()
    download_youtube_videos(sites_cards)
    extract_audios()
    speech2text(sites_cards)