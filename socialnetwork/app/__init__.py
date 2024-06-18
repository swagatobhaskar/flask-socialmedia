from flask import Flask
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

from extensions import db
from .models.user_models import User, Profile

from .blueprints.home.routes import home_bp
from .blueprints.user.routes import user_bp

from config import DevConfig

migrate = Migrate()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)

    app.config.from_object(DevConfig)

    db.init_app(app)
    migrate.init_app(app, db)

    # enable CSRF protection globally
    csrf.init_app(app)

    reg_blueprints(app)

    return app

def reg_blueprints(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(user_bp, url_prefix='/user')
 