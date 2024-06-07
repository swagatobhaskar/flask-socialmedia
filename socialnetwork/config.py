from os import path, environ
from dotenv import load_dotenv

# Specificy a `.env` file containing key/value config values
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

class Config:
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(Config):
    
    import os
    basedir = os.path.abspath(os.path.dirname(__file__))
    
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'mysocialmedia.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_PATH = environ.get('UPLOAD_PATH')

class ProdConfig(Config):
    DEBUG = False
