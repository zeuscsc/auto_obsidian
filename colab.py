from yt2txt import download_youtube_videos,extract_audios,get_sites_cards,speech2text
from articles2notes import generate as generate_notes
from snapshots4notes import match_notes_with_speeches, initialize as initialize_snapshots
import os

import articles2notes
articles2notes.NOTES_FOLDER=f"/content/drive/auto_obsidian"
articles2notes.ARTICLES_INDEXES_JSON_FILE_PATH=f"/content/drive/auto_obsidian/articles_indexes.json"
import video2snapshots
video2snapshots.SNAPSHOTS_FOLDER=f"/content/drive/auto_obsidian/snapshots"
import yt2txt
yt2txt.AUDIO_FOLDER=f"/content/drive/auto_obsidian/audios"
yt2txt.ARTICLES_FOLDER=f"/content/drive/auto_obsidian/articles"
import ytdl
ytdl.VIDEOS_FOLDER=f"/content/drive/auto_obsidian/videos"
os.makedirs("/content/drive/auto_obsidian", exist_ok=True)
sites_cards=get_sites_cards()
download_youtube_videos(sites_cards)
extract_audios()
speech2text(sites_cards)
generate_notes()
initialize_snapshots()
match_notes_with_speeches()