OBSIDIAN_FOLDER_NAME = "obsidian_notes"

def reset_root_folder(path:str):
    global ROOT_FOLDER,\
        VIDEOS_FOLDER,\
        AUDIO_FOLDER,\
        ARTICLES_FOLDER,\
        OBSIDIAN_FOLDER_NAME,\
        NOTES_FOLDER,\
        ARTICLES_INDEXES_JSON_FILE_PATH,\
        SNAPSHOTS_FOLDER,\
        LLM_RESPONSE_CACHE_FOLDER,\
        NOTES_WITH_SNAPSHOT_CACHE_FOLDER,\
        DATASETS_FOLDER,\
        LLM_FOLDER
    ROOT_FOLDER=path
    VIDEOS_FOLDER = f"{ROOT_FOLDER}videos"
    AUDIO_FOLDER = f"{ROOT_FOLDER}audios"
    ARTICLES_FOLDER = f"{ROOT_FOLDER}articles"
    NOTES_FOLDER = f"{ROOT_FOLDER}{OBSIDIAN_FOLDER_NAME}/markdown_notes"
    ARTICLES_INDEXES_JSON_FILE_PATH=f"{ROOT_FOLDER}articles_indexes.json"
    SNAPSHOTS_FOLDER = f"{ROOT_FOLDER}{OBSIDIAN_FOLDER_NAME}/snapshots"
    LLM_RESPONSE_CACHE_FOLDER = f"{ROOT_FOLDER}llm_response_cache"
    NOTES_WITH_SNAPSHOT_CACHE_FOLDER = f"{ROOT_FOLDER}note_with_snapshot_cache"
    DATASETS_FOLDER = f"{ROOT_FOLDER}datasets"
    LLM_FOLDER = f"{ROOT_FOLDER}llm"

reset_root_folder("./")