from flask import Blueprint, render_template, request, session, jsonify,redirect,url_for
from Kimo.config import load_config
from Kimo.services import ArticlesService as Article
from Kimo.services import PageService as Page
SENDTYPE=['create','update','delete']
ds=Blueprint('dashboard',__name__)

@ds.route('/dashboard',methods=['GET'])
def index():
    check_user = session.get('user_role')
    if check_user == 2:
        if request.method=='GET':  
            config =load_config('app','config')
            page_type=request.args.get("type", type=str)
            if not page_type:
                page_type ='home'
            if page_type =='manageArticle':
                categories = Article.get_all_categories()
                article_all = Article.get_all_articles()
                return render_template("dashboard.html",post=article_all,editor='1',categories=categories,config=config,pageType=page_type)
            if page_type =='editArticle':
                edit_id=request.args.get("id", type=int)
                result = Article.edit_article(edit_id)
                print(result)
                if not result:
                    return '查询不到文章'
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
                return render_template("dashboard.html",config=config,pageType=page_type,post=post)
            return render_template("dashboard.html",editor='1',id=id,config=config,pageType=page_type)
        
    return redirect(url_for('account.login'))
            



@ds.route('/dashboard/pages',methods=['POST'])
def page_control():
    id:int=request.json.get('id')
    methods_type=request.json.get('mtype')
    title=request.json.get('title')
    content=request.json.get('content')
    type=request.json.get('type')
    match methods_type:
        case 'create':
            return Page.create(title,content,type)
        case 'edit':  
            return Page.edit(id,title,content,type)
        case 'delete':
            return Page.delete(id)
        case _:
            return {
                "status":0,
                "msg":'不支持该格式'
            }