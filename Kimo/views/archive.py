import markdown
from flask import Blueprint, render_template, request, session, jsonify

from Kimo.config import load_config
from utils import db

bg=Blueprint('archive',__name__)

@bg.route('/',methods=['GET','POST'])
def index():
    dsb = session.get('user_role')
    post = db.fetchall('select * from blog')
    config =load_config('app','config')
    if request.method=='GET':
        return render_template('index.html',dashboard=dsb,config=config,posts=post)


    return post

@bg.route('/archive/<string:archive_title>',methods=['GET','POST'])
def archive(archive_title):
    config = load_config('app', 'config')
    archive_page = db.fetch_one('select * from blog where title=%s', [archive_title, ])
    if request.method=='GET':
        content = markdown.markdown(
    archive_page['content'],
            extensions=[
                "tables",
                "toc",
                "fenced_code",
                "pymdownx.superfences",
                "pymdownx.tasklist",
                "pymdownx.details",
                "pymdownx.inlinehilite",
            ]
)

        print(archive_page)
        return render_template('archive.html',config=config,article=archive_page,content=content)

    return archive


@bg.route('/post', methods=['GET', 'POST'])
def archive_post():
    check_user = session.get('user_role')
    if check_user == 0:
        config = load_config('app', 'config')
        if request.method == 'GET':
            return render_template('post.html', config=config)

        if request.method == 'POST':
            print('执行post')
            title = request.json.get('title')
            content = request.json.get('content')
            print(content)
            if not content:
                return jsonify({'message': '内容为空'}), 400

            try:
                db.increase('insert into blog(title,content) values (%s,%s)', [title, content])
            except Exception as e:
                return jsonify({'message': str(e)}), 500

            return jsonify({'message': 'ok'})

    return '无权访问'
