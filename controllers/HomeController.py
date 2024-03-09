from flask import Blueprint
home_bp = Blueprint('homecontroller', __name__)

@home_bp.route('/')
def hello():
    return "Hello from Home Page"