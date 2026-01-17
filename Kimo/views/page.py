from flask import Blueprint, render_template, request, session, jsonify,redirect,url_for

from Kimo.config import load_config
from Kimo.services import PageService
pg =Blueprint('page',__name__)

@pg.route('/<string:page_title>',methods =['GET'])
def view_page(page_title):
    if request.method == 'GET':
        config =load_config('app','config')
        page_result = PageService.get_by_name(page_title)
        print(page_result['content'])
        return render_template('page.html',p='1',config=config,page_title=page_title,page=page_result['content'])
    return '不支持'

@pg.route('/page/create',methods=['POST'])
def create_page():
    check_user = session.get('user_role')
    if check_user == 2:
        if request.method == 'POST':
            page_title = request.form['page_title']
            page_content = request.form['content']
            page_type = request.form['type']
            result= PageService.create(page_title, page_content, page_type)
            return {
                'status':result['status'],
                'msg':result['msg']
            }
    return {
        'status':False,
        'msg':'No'
    }

@pg.route('/page/update',methods=['POST'])
def update_page():
    check_user = session.get('user_role')
    if check_user == 2:
        if request.method == 'POST':
            page_title = request.form['page_title']
            page_content = request.form['content']
            page_type = request.form['type']
