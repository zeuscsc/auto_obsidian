import os
ROOT_FOLDER=os.path.dirname(os.path.abspath(__file__))
OBSIDIAN_FOLDER_NAME = "obsidian_notes"

def reset_root_folder(path:str):
    global VIDEOS_FOLDER,\
        AUDIO_FOLDER,\
        ARTICLES_FOLDER,\
        OBSIDIAN_FOLDER_NAME,\
        NOTES_FOLDER,\
        ARTICLES_INDEXES_JSON_FILE_PATH,\
        SNAPSHOTS_FOLDER,\
        CHAT_CACHE_FOLDER
    ROOT_FOLDER=path
    VIDEOS_FOLDER = f"{ROOT_FOLDER}/videos"
    AUDIO_FOLDER = f"{ROOT_FOLDER}/audios"
    ARTICLES_FOLDER = f"{ROOT_FOLDER}/articles"
    NOTES_FOLDER = f"{ROOT_FOLDER}/{OBSIDIAN_FOLDER_NAME}/markdown_notes"
    ARTICLES_INDEXES_JSON_FILE_PATH=f"{ROOT_FOLDER}/articles_indexes.json"
    SNAPSHOTS_FOLDER = f"{ROOT_FOLDER}/{OBSIDIAN_FOLDER_NAME}/snapshots"
    CHAT_CACHE_FOLDER = f"{ROOT_FOLDER}/chat_cache"