from flask import Blueprint, render_template, request, session, jsonify,redirect,url_for
from Kimo.config import load_config
from Kimo.services import ArticlesService as Article
ds=Blueprint('dashboard',__name__)

@ds.route('/dashboard',methods=['GET'])
def index():
    if request.method=='GET':  
        config =load_config('app','config')
        page_type=request.args.get("type", type=str)
        print(page_type,'dfddd')
        if not page_type:
            page_type ='home'
        if page_type =='home':
            article_all = Article.get_all_articles()
            return render_template("dashboard.html",post=article_all,editor='1',config=config,pageType=page_type)
        return render_template("dashboard.html",editor='1',config=config,pageType=page_type)
            


@ds.route('/dashboard/pages',methods=['GET'])
def pages_manage():
    return 'aaaa'