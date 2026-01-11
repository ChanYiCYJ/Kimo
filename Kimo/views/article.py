from flask import Blueprint, render_template, request, session, jsonify,redirect,url_for

from Kimo.config import load_config
from Kimo.services import ArticlesService as Article
bg=Blueprint('article',__name__)

@bg.route('/',methods=['GET','POST'])
def index():
    category_all = Article.get_all_categories()
    article_all = Article.get_all_articles()
    tag_all = Article.get_all_tags()
    config =load_config('app','config')
    if request.method=='GET':
        return render_template('index.html', page_title=config["title"],
                               page_subtitle=config["introduction"], config=config, posts=article_all,categorys=category_all,tags=tag_all)

    return article_all

@bg.route('/article/<int:article_id>',methods=['GET','POST'])
def article(article_id):

    article_page = Article.get_article_page(article_id)
    print(article_page)
    if request.method=='GET':
        return render_template('article.html', page_title=article_page['title'],
                               page_subtitle=f"Created: {article_page['created']}", article=article_page,content=article_page['content']
                               )

    return article_page



@bg.route('/post', methods=[ 'POST'])
def article_post():
        if request.method == 'POST':
            print('执行post')
            title = request.json.get('title')
            content = request.json.get('content')
            category_name = request.json.get('category_name')
            description = request.json.get('description')
            print(content)
            print(title)
            print(category_name)
            create_page=Article.send_article(title,content,category_name,description)
            if not create_page['status']:
                return jsonify({'message': create_page['msg']}),500    
            return jsonify({'message': create_page['msg']})



@bg.route('/tags', methods=['GET', 'POST'])
def tags():
        tag_all =Article.get_all_tags()
        if request.method == 'GET':
            config = load_config('app', 'config')
            return render_template('tag.html', tag_all=tag_all,config=config)
        return render_template('tag.html', tag_all=tag_all)

@bg.route('/category', methods=['GET', 'POST'])
def category():
    category_all = Article.get_all_categories()
    if request.method == 'GET':
        config = load_config('app', 'config')
        return render_template('category.html', category_all=category_all,config=config)
    return render_template('category.html', category_all=category_all)


@bg.route('/editor', methods=['GET','POST'])
def editor():
    check_user = session.get('user_role')
    if check_user == 2:
        if request.method == 'GET':
            categories = Article.get_all_categories()
            tag = Article.get_all_tags()
            return render_template('post.html', categories=categories, tags=tag)
        return render_template('post.html')

    return '无权访问', 400
@bg.route('/editor/<int:post_id>', methods=['GET', 'POST'])
def edit(post_id):
    print(post_id)
    result = Article.edit_article(post_id)
    print(result)
    return render_template('post.html', postId=result['id'], article=result['content'])



@bg.route('/delete', methods=['POST'])
def article_delete():
    check_user = session.get('user_role')
    if check_user == 0:
        post_id = request.json.get('post_id')
        result = Article.delete_article(post_id)
        if not result['status']:
            return jsonify({'message': result['msg']}),500
        return jsonify({'message': result['msg']})       
    return '无权访问', 400
