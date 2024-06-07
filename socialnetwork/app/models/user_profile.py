import enum
from datetime import datetime, timedelta
# from sqlalchemy import event
from sqlalchemy.sql import func

from extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False) # auto-fill 
    email = db.Column(db.String(30), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=False)
    # last_login = 
    profile = db.relationship('Profile', uselist=False, back_populates='user')

    def __repr__(self):
        return f"{self.id} {self.email}"

class SexEnum(enum.Enum):
    male = 'Male'
    female = 'Female'
    other = 'Other'

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=True)
    last_name = db.Column(db.String(30), nullable=True)
    dob = db.Column(db.DateTime, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    sex = db.Column(db.Enum(SexEnum), nullable=True)
    phone = db.Column(db.String(10), nullable=True, unique=True)
    state = db.Column(db.String(50), nullable=True)
    country = db.Column(db.String(50), nullable=True)
    nationality = db.Column(db.String(50), nullable=True)
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now(), nullable=True)
    avatar_path = db.Column(db.LargeBinary, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', back_populates='profile')

    def __repr__(self):
        return f"{self.f_name} {self.l_name} - {self.sex}"
