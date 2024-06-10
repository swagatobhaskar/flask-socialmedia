from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

home_bp = Blueprint('home', __name__, template_folder='templates', static_folder='static')

@home_bp.route('/')
@home_bp.route('/home')
def home():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)

@home_bp.route('/about')
def about():
    return render_template('about.html')
