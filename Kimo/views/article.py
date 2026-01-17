from flask import Blueprint, render_template, request, session, jsonify,redirect,url_for

from Kimo.config import load_config
from Kimo.services import ArticlesService as Article
bg=Blueprint('article',__name__)

@bg.route('/',methods=['GET','POST'])
def index():
    page= request.args.get("page", 1, type=int)
    category_all = Article.get_all_categories()
    result =Article.get_articles_lists(page)
    page_id=result['page_id']+1
    print(page_id)
    articles =result['articles']
    tag_all = Article.get_all_tags()
    total_articles =result['total_page']
    config =load_config('app','config')
    if request.method=='GET':
        return render_template('index.html', page_title=config["title"],
                               page_subtitle=config["ltitle"],total_pages=total_articles,pageId=page_id,config=config, posts=articles,categorys=category_all,tags=tag_all)

    return articles


@bg.route('/article/<int:article_id>',methods=['GET','POST'])
def article(article_id):
    config = load_config('app', 'config')
    article_page = Article.get_article_page(article_id)
    print(article_page)
    if request.method=='GET':
        return render_template('article.html',config=config , page_title=article_page['title'],
                               page_subtitle=f"Created: {article_page['created']}", article=article_page,content=article_page['content']
                               )

    return article_page

@bg.route('/post', methods=[ 'POST'])
def article_post():
    check_user = session.get('user_role')
    if check_user == 2:
        if request.method == 'POST':
            print('执行post')
            title = request.json.get('title')
            content = request.json.get('content')
            category_name = request.json.get('category_name')
            description = request.json.get('description')
            cover_image =request.json.get('coverUrl')
            id= None
            print(content)
            print(title)
            print(category_name)
            create_page=Article.send_article(title,content,category_name,description,cover_image,id)
            if not create_page['status']:
                return jsonify({'message': create_page['msg']}),500    
            return jsonify({'message': create_page['msg']})
    return jsonify({'message': '无权'}),500  

@bg.route('/articles/update',methods=['POST'])
def article_update(): 
    check_user = session.get('user_role')
    if check_user == 2:
     if request.method == 'POST':
        title = request.json.get('title')
        content = request.json.get('content')
        category_name = request.json.get('category_name')
        description = request.json.get('description')
        cover_image =request.json.get('coverUrl')
        id= request.json.get('postId')
        create_page=Article.send_article(title,content,category_name,description,cover_image,id)
        if not create_page['status']:
            return jsonify({'message': create_page['msg']}),500    
        return jsonify({'message': create_page['msg']})
    return jsonify({'message': '无权'}),500  

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
            return render_template('createArticle.html', categories=categories, tags=tag)
        return render_template('post.html')

    return redirect(url_for('account.login'))
@bg.route('/editor/<int:post_id>', methods=['GET', 'POST'])
def edit_article(post_id):
    check_user = session.get('user_role')
    if check_user == 2:
        print(post_id)
        categories = Article.get_all_categories()
        tag = Article.get_all_tags()
        result = Article.edit_article(post_id)
        ca_id= result['category_id']
        ca_name= Article.get_category_name_by_id(ca_id)
        print(result)
        post = {
        'id' :result['id'],
        'title': result['title'],
        'content': result['content'],
        'category_name': ca_name,
        'category_id': ca_id,
        'cover_url': result['cover_image'],
    }
        print(post)
        print(post)
        return render_template('createArticle.html', post=post,categories=categories, tags=tag)
    return redirect(url_for('account.login'))


@bg.route('/article/delete', methods=['POST'])
def article_delete():
    check_user = session.get('user_role')
    if check_user == 2:
        post_id = request.json.get('post_id')
        result = Article.delete_article(post_id)
        if not result['status']:
            return jsonify({'message': result['msg']}),500
        return jsonify({'message': result['msg']})       
    return jsonify({'message': '无权'}),500 

@bg.route('/upload/image',methods=['POST'])
def upload_image():
    check_user = session.get('user_role')
    if check_user == 2:
        if request.method == 'POST':
            file =request.files.get('file')
            result=Article.upload_image(file)
            return jsonify({'status':result['status'],'message':result['msg'],'url':result['url']})
    return jsonify({'message': '无权'}),500

@bg.route('/upload/image/vditor',methods=['POST'])
def upload_image_by_vditor():
    check_user = session.get('user_role')
    if check_user == 2:
        if request.method == 'POST':
            file =request.files.get('file')
            result=Article.upload_image_by_vditor(file)
            return result 
    return jsonify({'message': '无权'}),500 
        
@bg.route('/dashboard/article/manage',methods=['GET'])
def manage():
    config = load_config('app', 'config')
    check_user = session.get('user_role')
    if check_user == 2:
        if request.method =='GET':
            article_all = Article.get_all_articles()
            return render_template("article_manage.html",config=config ,post=article_all)
    return redirect(url_for('account.login'))