from flask import Blueprint, render_template, redirect, request, url_for

from app.models.user_models import User, Profile
from .forms.login_form import LoginForm

user_bp = Blueprint('main', __name__, template_folder='templates')

@user_bp.route("/signup")
def home():
    return "<p> Hello, World!</p>"

@user_bp.route('/login', methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if request.method == "POST":
        if login_form.validate_on_submit():
            user = User.query.filter_by(email=login_form.email.data).first()
            if user and user.check_password(login_form.password.data):
                # successful login
                return redirect(url_for('/'))
            else:
                return redirect(request.url) # redirect to login page
    return render_template('login.html', form=login_form)

@user_bp.route("profile/<int:id>")
def profile(id):
    user_profile = Profile.query.filter_by(user_id=id).first()
    profile_id = user_profile.id
    return f"Profile id: {profile_id}"
