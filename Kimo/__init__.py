import os

from flask import Flask


def create_app():
    app = Flask(__name__)
    app.secret_key= os.urandom(24)

    from  .views import account
    from .views import archive
    app.register_blueprint(account.ac)
    app.register_blueprint(archive.bg)
    return app