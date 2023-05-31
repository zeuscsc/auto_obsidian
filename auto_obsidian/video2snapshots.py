from PIL import Image
import os
import glob
import cv2

from .folders import SNAPSHOTS_FOLDER,VIDEOS_FOLDER,OBSIDIAN_FOLDER_NAME,ROOT_FOLDER
from .img4qna import get_answer,object_decision

video=None

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

def calcuate_snapshot_time(start:int,end:int):
    if end-start<2:
        return -1
    snapshot_time=start+((end-start)/2)
    return snapshot_time
def get_snapshot_time(video_id:str,start:int,end:int):
    return start+((end-start)/2)
def get_best_snapshot_time(video_id:str,start:int,end:int):
    snapshot_time=calcuate_snapshot_time(start,end)
    if snapshot_time<0:
        return snapshot_time
    if is_good_note_snapshot(extract_frame(video_id,snapshot_time)):
        return snapshot_time
    else:
        lhs=snapshot_score(extract_frame(video_id,calcuate_snapshot_time(start,snapshot_time)))
        rhs=snapshot_score(extract_frame(video_id,calcuate_snapshot_time(snapshot_time,end)))
        if lhs>rhs:
            return get_best_snapshot_time(video_id,start,snapshot_time)
        elif lhs<rhs:
            return get_best_snapshot_time(video_id,snapshot_time,end)
        elif lhs==rhs==-1:
            return -1
        else:
            return snapshot_time
def get_snapshot_path(video_id:str,snapshot_time:int):
    snapshot_time_str=convert_seconds_to_time(snapshot_time)
    snapshot_time_str4file=snapshot_time_str.replace(":","-")
    snapshot_file_path=f"{SNAPSHOTS_FOLDER}/{video_id}/{snapshot_time_str4file}.png"
    return snapshot_file_path

def check_video(video_id:str):
    if video is None:
        load_video(video_id)
    if loaded_video_id!=video_id:
        unload_video()
        load_video(video_id)
def extract_frame(video_id:str,snapshot_time:int):
    if snapshot_time<0:
        return None
    check_video(video_id)
    fps = video.get(cv2.CAP_PROP_FPS)
    frame_index = int(snapshot_time * fps)
    video.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
    ret, frame = video.read()
    if not ret:
        raise Exception("Error reading frame")
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(frame_rgb)
    return pil_image
def extract_snapshot(video_id:str,start:int=None,end:int=None):
    check_video(video_id)
    snapshot_time=get_best_snapshot_time(video_id,start,end)
    return extract_frame(video_id,snapshot_time)

def save_snapshot(video_id:str,start:int,end:int):
    # snapshot_time=get_best_snapshot_time(video_id,start,end)
    snapshot_time=get_snapshot_time(video_id,start,end)
    if snapshot_time<0:
        return None
    frame=extract_frame(video_id,snapshot_time)
    snapshot_file_path=get_snapshot_path(video_id,snapshot_time)
    os.makedirs(SNAPSHOTS_FOLDER, exist_ok=True)
    os.makedirs(f"{SNAPSHOTS_FOLDER}/{video_id}", exist_ok=True)
    # cv2.imwrite(snapshot_file_path, frame)
    frame.save(snapshot_file_path)
    return start,snapshot_file_path
def get_relative_image_path(snapshot_file_path:str):
    return snapshot_file_path.replace(f"{OBSIDIAN_FOLDER_NAME}/", "").replace(f"{ROOT_FOLDER}","").replace("./", "")

def is_good_note_snapshot(frame:Image):
    if frame is None:
        return False
    if object_decision(get_answer(frame,"What is it?")):
        return True
    if get_answer(frame,"Is there any people inside?") == "yes":
        if get_answer(frame,"Is the image mostly a person?") == "yes":
            return False
    
    return False
def snapshot_score(frame:Image):
    if frame is None:
        return -1
    score =get_answer(frame,"From the scale of 1 to 10, how good is this image for note taking?")
    if score.isdigit():
        score=int(score)
    else:
        likely=get_answer(frame,"Is this image likely to be a good note?")
        if likely=="yes":
            score=10
        elif likely=="no":
            score=1
    score = int(score)
    if score is None:
        return -1
    return score