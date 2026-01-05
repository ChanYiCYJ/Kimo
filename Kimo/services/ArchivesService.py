from Kimo.models import archives
import markdown
def get_all_archives():
    return archives.get_all_archives()

def get_all_categories():
    return archives.get_all_categoies()

def get_all_tags():
    return archives.get_all_tags()

def get_category_name_by_id(id):
    result = archives.get_category_name_by_id(id)
    if not result :
        return []
    return result['name']

def get_archive_page(archive_id):
    result =archives.get_archive_by_id(archive_id)
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

def send_archive(title,content,category_name):
    if not (title and content):
        return {
            "status":False,
            "msg":'缺少(标题、内容)'
        }
    if not category_name:
        category_id = None
    else:
        category_id = archives.get_category_id_by_name(category_name)
        if not category_id:
           category_result= archives.create_category(category_name)
        if not category_result:
               return{
                   "status":False,
                    "msg":'创建分类名失败'
               }
        return{
                   "status":True,
                    "msg":'创建分类名成功'
               }
    archive_result=archives.create_archive(title,content,category_id)
    if not archive_result:
        return{
                   "status":False,
                    "msg":'创建文章失败'
               }
    return{
            "status":True,
            "msg":'创建文章成功'
               }
          
def edit_archive(id):
    return archives.get_archive_by_id(id)

def delete_archive(id):
    check = archives.get_archive_by_id(id)
    if not check:
        return {
            "status": False,
            "msg":"没有找到需要删除的文章"
        }
    delete_result=archives.delete_archive(id)
    if not delete_result:
        return {
            "status": False,
            "msg":"删除失败"
        }
    return {
        "status": True,
        "msg":'删除成功'
    }