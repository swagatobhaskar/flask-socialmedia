from flask import Blueprint, render_template

user_bp = Blueprint('main', __name__, template_folder='templates')

@user_bp.route("/signup")
def home():
    return "<p> Hello, World!</p>"

# @user_bp.route("profile/<id>")
# def profile():
#     pass