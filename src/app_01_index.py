from flask import Blueprint

appBlueprint = Blueprint("home", __name__)

@appBlueprint.route('/')
def index():
    return 'Hello world'