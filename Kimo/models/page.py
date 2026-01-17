from utils import db

def create_page(name,content,page_type):
    result= db.implement('insert into page(name,content,type) values(%s,%s,%s)',[name,content,page_type]) or []
    return result

def edit_page(page_id,name,content,page_type):
    return 'create'

def get_page_by_id(page_id):
    result =db.fetch_one('select * from page where id=%s',[page_id])
    return result

def get_page_by_name(name):
    result =db.fetch_one('select * from page where name=%s',[name])
    return result

def delete_page():
    return 'delete_page'

