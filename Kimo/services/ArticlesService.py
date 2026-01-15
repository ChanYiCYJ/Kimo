from Kimo.models import articles
import markdown
from utils import pinyin
from bs4 import BeautifulSoup as bs
from utils import upload
import math
def get_all_articles():
    return articles.get_all_articles()

def get_all_categories():
    return articles.get_all_categoies()

def get_all_tags():
    return articles.get_all_tags()

def get_category_name_by_id(id):
    result = articles.get_category_name_by_id(id)
    if not result :
        return []
    return result['name']

def get_article_page(article_id):
    result =articles.get_article_by_id(article_id)
    print(result)
    if not result:
        return{
            "status": False,
            "msg" : '文章不存在'
        }
    category_name=get_category_name_by_id(result['category_id'])
    content = markdown.markdown(
            result['content'],
            extensions=[
                "tables",
                "toc",
                "fenced_code",
                "pymdownx.superfences",
                "pymdownx.tasklist",
                "pymdownx.details",
                "pymdownx.inlinehilite",
            ]
)
    return{
        "status":True,
        "title" :result['title'],
        "content" :content,
        "created" : result['created'],
        "category_name":category_name,
    }

def get_articles_lists(page):
    perpage = 5
    page_id=page-1
    offset = page_id * perpage
    result = articles.get_articles_lists(limit=perpage, offset=offset)
    all_articles_length = articles.get_all_articles_count()['COUNT(*)']
    total_page = math.ceil(all_articles_length / perpage)
    return {
        "articles": result,
        "total_page": total_page,
        "page_id" : page_id
    }

def send_article(title, content, category_name, description, cover_image,id):
    # 1. 基础校验
    if not title or not content:
        return {
            "status": False,
            "msg": "缺少(标题、内容)"
        }

    # 2. 自动生成摘要
    if not description:
        html = markdown.markdown(content)
        soup = bs(html, "html.parser")
        text = soup.get_text(separator=" ", strip=True)
        description = text[:20]

    # 3. 封面图兜底
    cover_image = cover_image or None

    # 4. 分类处理
  
    if category_name:
        category = articles.get_category_id_by_name(category_name)

        if not category:
        # 不存在 → 创建
            articles.create_category(
            category_name,
            pinyin.translate(category_name)
        )
        # 再查一次
        category = articles.get_category_id_by_name(category_name)

        category_id = category['id']
    else:
        category_id = None

    print(id)
    if not id:
        # 5. 创建文章
        article_result = articles.create_article(
            title,
            content,
            category_id,
            description,
            cover_image
        )
        
    article_result = articles.update_article(title, content, category_id, description, cover_image, id)
    if not article_result:
            return {
                "status": False,
                "msg": "编辑文章失败"
            }
    return {
            "status": True,
            "msg": "编辑文章成功",
            "article_id": article_result
        }

def edit_article(id):
    return articles.get_article_by_id(id)

def delete_article(id):
    check = articles.get_article_by_id(id)
    if not check:
        return {
            "status": False,
            "msg":"没有找到需要删除的文章"
        }
    delete_result=articles.delete_article(id)
    if not delete_result:
        return {
            "status": False,
            "msg":"删除失败"
        }
    return {
        "status": True,
        "msg":'删除成功'
    }

def upload_image(file):
    return upload.upload_file(file)

def upload_image_by_vditor(file):
    result=upload.upload_file(file)
    if result['status'] == 1:
        return{
            "code": 0,
            "msg": "ok",
            "data": {
              "errFiles": [],
               "succMap": {
                 result['filename']: f"/static/uploads/{result['filename']}"
                }
            }
        }