import markdown
from flask import Blueprint, render_template, request, session, jsonify

from Kimo.config import load_config
from utils import db

bg=Blueprint('archive',__name__)

@bg.route('/',methods=['GET','POST'])
def archive_list():
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
    config = load_config('app', 'config')
    if request.method == 'GET':
        return render_template('post.html', config=config)

    data = request.get_json()
    content = data.get('content')

    if not content:
        return jsonify({'message': '内容为空'}), 400

    try:
        db.fetch_one('insert into blog values (%s)', [content])
    except Exception as e:
        return jsonify({'message': str(e)}), 500

    return jsonify({'message': 'ok'})
