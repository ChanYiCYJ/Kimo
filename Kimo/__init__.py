import os
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.secret_key= os.urandom(24)

    from  .views import account
    from .views import article
    from .views import page
    app.register_blueprint(account.ac)
    app.register_blueprint(article.bg)
    app.register_blueprint(page.pg)
    return app