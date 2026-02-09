import math
from Kimo.models import articles,pages
class Base:
    def search(self,text):
        raise NotImplementedError
    def count(self, peerage=5):
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

class Service:
    def __init__(self,search_peerage=5):
        self.peerage = search_peerage
        self.map ={
            'articles':articles,
            'pages':pages,
        }

    def search(self,keyword,search_type:str='articles',page:int=1):
        if not keyword:
            return {
                "status":False,
                "msg":'无输入内容'
            }
        if search_type not in self.map:
            return {
                "status":False,
                "msg":"不支持的类型"
            }
        searcher = self.map[search_type]
        offset = (page - 1) * self.peerage
        result =searcher.search(keyword)
        return result
