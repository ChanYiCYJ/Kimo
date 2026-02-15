from utils import db

def create_page(name,content,page_type):
    result= db.implement('insert into page(name,content,type) values(%s,%s,%s)',[name,content,page_type]) or []
    return result

def edit_page(page_id,name,content,page_type):
    result =db.implement('update page set name=%s,content=%s,type=%s where id=%s',[name,content,page_type,page_id]) or[]
    return result
def get_page_by_id(page_id):
    result =db.fetch_one('select * from page where id=%s',[page_id]) or[]
    return result

def get_page_by_name(name):
    result =db.fetch_one('select * from page where name=%s',[name]) or None
    return result

def get_like_name(name):
    result = db.fetch_one('select * from page where name like %s', [name]) or None
    return result

def delete_page(page_id):
    result =db.implement(
        'delete from page where id=%s',[page_id])
    return result

def get_all_page(limit=5, offset=0):
    return db.fetchall('select * from page LIMIT %s OFFSET %s;', (limit, offset))

def get_all_page_count():
    return db.fetch_one('select count(*) from page;')