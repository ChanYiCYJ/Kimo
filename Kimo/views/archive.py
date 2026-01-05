from flask import Blueprint, render_template, request, session, jsonify,redirect,url_for

from Kimo.config import load_config
from utils import db
from Kimo.services import ArchivesService as Archive
bg=Blueprint('archive',__name__)

@bg.route('/',methods=['GET','POST'])
def index():
    category_all = Archive.get_all_categories()
    archive_all = Archive.get_all_archives()
    tag_all = Archive.get_all_tags()
    config =load_config('app','config')
    if request.method=='GET':
        return render_template('index.html', page_title=config["title"],
                               page_subtitle=config["introduction"], config=config, posts=archive_all,categorys=category_all,tags=tag_all)

    return archive_all

@bg.route('/archive/<int:archive_id>',methods=['GET','POST'])
def archive(archive_id):

    archive_page = Archive.get_archive_page(archive_id)
    print(archive_page)
    if request.method=='GET':
        return render_template('archive.html', page_title=archive_page['title'],
                               page_subtitle=f"Created: {archive_page['created']}", article=archive_page,content=archive_page['content']
                               )

    return archive



@bg.route('/post', methods=[ 'POST'])
def archive_post():
        if request.method == 'POST':
            print('执行post')
            title = request.json.get('title')
            content = request.json.get('content')
            category_name = request.json.get('category_name')
            print(content)
            print(title)
            print(category_name)
            create_page=Archive.send_archive(title,content,category_name)
            if not create_page['status']:
                return jsonify({'message': create_page['msg']}),500    
            return jsonify({'message': create_page['msg']})



@bg.route('/tags', methods=['GET', 'POST'])
def tags():
        tag_all = db.fetchall('select * from tags ', )
        if request.method == 'GET':
            config = load_config('app', 'config')
            return render_template('tag.html', tag_all=tag_all,config=config)
        return render_template('tag.html', tag_all=tag_all)

@bg.route('/category', methods=['GET', 'POST'])
def category():
    category_all = db.fetchall('select * from categories ', )or []
    if request.method == 'GET':
        config = load_config('app', 'config')
        return render_template('category.html', category_all=category_all,config=config)
    return render_template('category.html', category_all=category_all)


@bg.route('/editor', methods=['GET','POST'])
def editor():
    check_user = session.get('user_role')
    if check_user == 2:
        if request.method == 'GET':
            categories = db.fetchall('select * from categories ', )
            tag = db.fetchall('select * from tags ', )
            return render_template('post.html', categories=categories, tags=tag)
        return render_template('post.html')

    return '无权访问', 400
@bg.route('/editor/<int:post_id>', methods=['GET', 'POST'])
def edit(post_id):
    print(post_id)
    result = Archive.edit_archive(post_id)
    print(result)
    return render_template('post.html', postId=result['id'], article=result['content'])



@bg.route('/delete', methods=['POST'])
def archive_delete():
    check_user = session.get('user_role')
    if check_user == 0:
        post_id = request.json.get('post_id')
        result = Archive.delete_archive(post_id)
        if not result['status']:
            return jsonify({'message': result['msg']}),500
        return jsonify({'message': result['msg']})       
    return '无权访问', 400
