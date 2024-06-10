from flask import Blueprint, render_template

user_bp = Blueprint('main', __name__)

@user_bp.route("/")
def home():
    return "<p> Hello, World!</p>"