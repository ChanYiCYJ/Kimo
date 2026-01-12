from utils import db

def get_all_articles():
    return db.fetchall('SELECT a.id,a.title,a.content,a.created,a.description,a.cover_image,c.name AS category_name FROM articles a LEFT JOIN categories c ON a.category_id = c.id ORDER BY a.created DESC;')or []

def get_article_by_title(titile):
    return db.fetch_one('SELECT * FROM articles WHERE title LIKE %s',[titile])or []

def get_article_by_id(id):
    return db.fetch_one('SELECT * FROM articles WHERE id=%s',[id])or []

def create_article(title,content,category_id,description,cover_image):
    return db.implement('insert into articles(title,content,category_id,description,cover_image) values (%s,%s,%s,%s,%s)', [title, content,category_id,description,cover_image])or []

def delete_article(id):
    return db.implement('delete from articles where id=%s', [id, ])

def get_all_categoies():
    return db.fetchall('select * from categories')

def get_category_id_by_name(category_name):
    return db.fetch_one('select id from categories where name=%s', [category_name,])or[]

def get_category_name_by_id(category_id):
    return db.fetch_one('select * from categories where id=%s', [category_id,])or[]

def create_category(name,slug):
    return db.implement('insert into categories(name,slug) values (%s,%s)',[name,slug])or []

def get_all_tags():
    return db.fetchall('select * from tags ', )or []





