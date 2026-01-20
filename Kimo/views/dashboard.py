from flask import Blueprint, render_template, request, session, jsonify,redirect,url_for
from Kimo.config import load_config
from Kimo.services import ArticlesService as Article
ds=Blueprint('dashboard',__name__)

@ds.route('/dashboard',methods=['GET'])
def index():
    check_user = session.get('user_role')
    if check_user == 2:
        if request.method=='GET':  
            config =load_config('app','config')
            page_type=request.args.get("type", type=str)
            id=request.args.get("id", type=int)
            print(page_type,id,'dfddd')
            if not page_type:
                page_type ='home'
            if page_type =='manageArticle':
                categories = Article.get_all_categories()
                article_all = Article.get_all_articles()
                return render_template("dashboard.html",post=article_all,editor='1',categories=categories,config=config,pageType=page_type)
            return render_template("dashboard.html",editor='1',id=id,config=config,pageType=page_type)
        
    return redirect(url_for('account.login'))
            


@ds.route('/dashboard/pages',methods=['GET'])
def pages_manage():
    return 'aaaa'