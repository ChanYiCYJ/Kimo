from utils import db

def get_all_archives():
    return db.fetchall('SELECT a.id,a.title,a.content,a.created,c.name AS category_name FROM archives a LEFT JOIN categories c ON a.category_id = c.id ORDER BY a.created DESC;')or []

def get_archive_by_title(titile):
    return db.fetch_one('SELECT * FROM archives WHERE title LIKE %s',[titile])or []

def get_archive_by_id(id):
    return db.fetch_one('SELECT * FROM archives WHERE id=%s',[id])or []

def create_archive(title,content,category_id,description):
    return db.implement('insert into archives(title,content,category_id) values (%s,%s,%s)', [title, content,category_id])or []

def delete_archive(id):
    return db.implement('delete from archives where id=%s', [id, ])

def get_all_categoies():
    return db.fetchall('select * from categories')

def get_category_id_by_name(category_name):
    return db.fetch_one('select id from categories where name=%s', [category_name,])or[]

def get_category_name_by_id(category_id):
    return db.fetch_one('select * from categories where id=%s', [category_id,])or[]

def create_category(name):
    return db.implement('insert into categories(name,slug) values (%s,%s)',[name,name])or []

def get_all_tags():
    return db.fetchall('select * from tags ', )or []





