from yt2txt import download_youtube_videos,extract_audios,get_sites_cards,speech2text
from articles2notes import generate as generate_notes
from snapshots4notes import add_snapshot4notes_with_speeches, initialize as initialize_snapshots
from links4notes import link_all_notes

if __name__ == '__main__':
    sites_cards=get_sites_cards()
    download_youtube_videos(sites_cards)
    extract_audios()
    speech2text(sites_cards)
    generate_notes()
    initialize_snapshots()
    add_snapshot4notes_with_speeches()
    link_all_notes()