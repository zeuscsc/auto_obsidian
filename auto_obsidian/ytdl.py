import subprocess
import os
import re
import glob

from .folders import VIDEOS_FOLDER

def get_file_in_directory(filename_without_extension:str):
    matching_files = glob.glob(f"{VIDEOS_FOLDER}/{filename_without_extension}.*")
    if len(matching_files) == 0:
        return None
    return matching_files[0]
def download(video_id:str):
    video_url = "https://www.youtube.com/watch?v=" + video_id
    output_folder = VIDEOS_FOLDER
    os.makedirs(output_folder, exist_ok=True)
    if get_file_in_directory(video_id) is not None:
        print(f"Skipping {get_file_in_directory(video_id)} because it already exists")
        return
    if get_file_in_directory(video_id) is None:
        command = f"yt-dlp -o {output_folder}/%(id)s.%(ext)s {video_url}"
        print(f"Running command: {command}")
        subprocess.call(command, shell=True)

def extract_video_id(url:str):
    pattern = r"(?:v=|v\/|vi=|vi\/|youtu.be\/|\/v\/|embed\/|\/u\/\w\/|e\/|watch\?v=|\&v=|\?v=)([\w-]+)"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        return None
