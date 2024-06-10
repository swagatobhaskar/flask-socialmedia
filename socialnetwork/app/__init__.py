from flask import Flask
from flask_migrate import Migrate

from extensions import db
from .models.user_profile import User, Profile
from .user.routes import user_bp

from config import DevConfig

migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config.from_object(DevConfig)

    db.init_app(app)
    migrate.init_app(app, db)

    reg_blueprints(app)

    return app

def reg_blueprints(app):
    app.register_blueprint(user_bp)
