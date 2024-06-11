from flask import Blueprint, render_template
from app.models.user_models import User, Profile

user_bp = Blueprint('main', __name__, template_folder='templates')

@user_bp.route("/signup")
def home():
    return "<p> Hello, World!</p>"

@user_bp.route("profile/<int:id>")
def profile(id):
    user_profile = Profile.query.filter_by(user_id=id).first()
    profile_id = user_profile.id
    return f"Profile id: {profile_id}"
