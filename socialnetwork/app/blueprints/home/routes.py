from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

# from blueprints.user.forms.login_form import LoginForm --> module blueprints not found
from ..user.forms.login_form import LoginForm

home_bp = Blueprint('home', __name__, template_folder='templates', static_folder='static', static_url_path='/home/static/')

@home_bp.route('/')
@home_bp.route('/home')
def home():
    login_form = LoginForm()
    try:
        return render_template('index.html', form=login_form)
    except TemplateNotFound:
        abort(404)

@home_bp.route('/about')
def about():
    return render_template('about.html')
