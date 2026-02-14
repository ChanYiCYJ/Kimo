import math
from Kimo.models import articles,pages,data
class Base:
    def search(self,text):
        raise NotImplementedError
    def count(self, page_size=5):
        raise NotImplementedError

class Article(Base):
    def search(self,text):
        return articles.get_all_like_title(text)
    def count(self, peerage=5):
        all_articles_length = articles.get_all_articles_count()
        return math.ceil(all_articles_length['COUNT(*)'] / peerage)
class Page(Base):
    def search(self,text):
        return pages.get_like_name(text)
class All(Base):
    def search(self, text):
        result = data.search_all_data(text)
        return {'articles': result['articles'], 'pages': result['pages']}

class Service:
    def __init__(self, page_size=5):
        self.page_size = page_size
        self.map = {
            'articles': Article(),
            'pages': Page(),
            'all': All(),
        }

    def search(self, keyword, search_type='articles', page=1):
        if not keyword:
            return {"status": False, "msg": "无输入内容"}

        if search_type not in self.map:
            return {"status": False, "msg": "不支持的类型,所支持搜索的类型有all,articles,pages"},400

        searcher = self.map[search_type]
        data = searcher.search(keyword)   
        return {
            "status": True,
            "keyword" : keyword,
            "data": data,
        }

