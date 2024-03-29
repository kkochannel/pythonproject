import os
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ.get('SECRET_KEY')

    from . import app_01_index
    app.register_blueprint(app_01_index.appBlueprint)

    return app