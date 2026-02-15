from Kimo.models import articles,pages
def search_all_data(keyword):
    article_result = articles.get_all_like_title(keyword)
    page_result = pages.get_like_name(keyword)
    return {
        'articles': article_result,
        'pages': page_result
    }