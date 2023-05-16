import json
import subprocess
import os
import glob
import cv2

from .ytdl import VIDEOS_FOLDER,extract_video_id

SNAPSHOTS_FOLDER = "obsidian_notes/snapshots"

def get_file_in_directory(filename_without_extension:str):
    matching_files = glob.glob(f"{VIDEOS_FOLDER}/{filename_without_extension}.*")
    return matching_files[0]
def convert_seconds_to_time(seconds):
    seconds = int(seconds)
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
def load_video(video_id):
    global video,loaded_video_id
    loaded_video_id=video_id
    video_file_path=get_file_in_directory(video_id)
    video = cv2.VideoCapture(video_file_path)
    if not video.isOpened():
        raise Exception("Error opening video file")
    return video
def unload_video():
    global video,video_id
    video.release()
    video=None
    video_id=None

def get_snapshot_time(start:float,end:float):
    snapshot_time=start+((end-start)/2)
    return snapshot_time
def get_snapshot_path(video_id:str,snapshot_time:float):
    snapshot_time_str=convert_seconds_to_time(snapshot_time)
    snapshot_time_str4file=snapshot_time_str.replace(":","-")
    snapshot_file_path=f"{SNAPSHOTS_FOLDER}/{video_id}/{snapshot_time_str4file}.png"
    return snapshot_file_path

def extract_snapshot(video_id:str,start:float,end:float):
    if video is None:
        load_video(video_id)
    if loaded_video_id!=video_id:
        unload_video()
        load_video(video_id)
    snapshot_time=get_snapshot_time(start,end)
    fps = video.get(cv2.CAP_PROP_FPS)
    frame_index = int(snapshot_time * fps)
    snapshot_file_path=get_snapshot_path(video_id,snapshot_time)
    video.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
    ret, frame = video.read()
    if not ret:
        raise Exception("Error reading frame")
    os.makedirs(SNAPSHOTS_FOLDER, exist_ok=True)
    os.makedirs(f"{SNAPSHOTS_FOLDER}/{video_id}", exist_ok=True)
    cv2.imwrite(snapshot_file_path, frame)
    return snapshot_file_path

# def extract_snapshot(video_id:str, start:float, end:float,overwrite=False):
#     snapshot_time=start+((end-start)/2)
#     os.makedirs(SNAPSHOTS_FOLDER, exist_ok=True)
#     video_file_path=get_file_in_directory(video_id)
#     os.makedirs(f"{SNAPSHOTS_FOLDER}/{video_id}", exist_ok=True)
#     snapshot_time_str=convert_seconds_to_time(snapshot_time)
#     snapshot_time_str4file=snapshot_time_str.replace(":","-")
#     snapshot_file_name=f"{SNAPSHOTS_FOLDER}/{video_id}/{snapshot_time_str4file}.png"
#     if overwrite:
#         command=f"ffmpeg -i {video_file_path} -ss {snapshot_time_str} -vframes 1 -y {snapshot_file_name}"
#     else:
#         command=f"ffmpeg -i {video_file_path} -ss {snapshot_time_str} -vframes 1 -n {snapshot_file_name}"
#     subprocess.call(command, shell=True)
#     return snapshot_file_name
def extract_all():
    os.makedirs(SNAPSHOTS_FOLDER, exist_ok=True)
    articles_indexes_json_file_path = "./articles_indexes.json"
    with open(articles_indexes_json_file_path, "r",encoding="utf8") as articles_indexes_json_file:
        articles_indexes_json_data = json.load(articles_indexes_json_file)
        
        for key in articles_indexes_json_data:
            article_index=articles_indexes_json_data[key]
            url=article_index["url"]
            article_path=article_index["file_path"]
            video_id=extract_video_id(url)
            video_file_path=get_file_in_directory(video_id)
            os.makedirs(f"{SNAPSHOTS_FOLDER}/{video_id}", exist_ok=True)
            with open(article_path, "r",encoding="utf8") as article_file:
                article_json_data = json.load(article_file)
                segments=article_json_data["segments"]
                for segment in segments:
                    start=segment["start"]
                    end=segment["end"]
                    snapshot_time=start+((end-start)/2)
                    snapshot_time_str=convert_seconds_to_time(snapshot_time)
                    snapshot_time_str4file=snapshot_time_str.replace(":","-")
                    snapshot_file_name=f"{SNAPSHOTS_FOLDER}/{video_id}/{snapshot_time_str4file}.png"
                    command=f"ffmpeg -i {video_file_path} -ss {snapshot_time_str} -vframes 1 {snapshot_file_name}"
                    subprocess.call(command, shell=True)
                    pass
if __name__ == "__main__":
    # extract_all()
    load_video("3-_s2SCXh7s")
    extract_snapshot("3-_s2SCXh7s",0, 10)
    unload_video()
    load_video("3A3OuTdsPEk")
    extract_snapshot("3A3OuTdsPEk",0, 10)
    unload_video()