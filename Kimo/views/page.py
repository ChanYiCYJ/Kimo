from flask import Blueprint, render_template, request, session, jsonify,redirect,url_for

from Kimo.config import load_config
from Kimo.services import PageService
pg =Blueprint('page',__name__)

@pg.route('/<string:page_title>',methods =['GET'])
def view_page(page_title):
    if request.method == 'GET':
        page_result = PageService.get_by_name(page_title)
        print(page_result['content'])
        return render_template('page.html',page_title=page_title,page=page_result['content'])
    return '不支持'