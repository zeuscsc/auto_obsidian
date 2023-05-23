from .articles2notes import load_articles_indexes

def group_all():
    articles_indexes = load_articles_indexes()
    for key in articles_indexes:
        article_index=articles_indexes[key]
        
        article_title=str(article_index["title"])