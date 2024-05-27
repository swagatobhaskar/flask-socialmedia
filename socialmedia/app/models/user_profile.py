import enum
from datetime import datetime, timedelta
# from sqlalchemy import event
from sqlalchemy.sql import func

from ..extensions import db

class SexEnum(enum.Enum):
    male = 'Male'
    female = 'Female'
    other = 'Other'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), nullable=False)
    password1 = ''
    password2 = ''
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=False)
    profile = db.relationship('Profile', uselist=False, back_populates='user')

    def __repr__(self):
        return f"{self.id} {self.email}"
    
class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(30), nullable=False)
    l_name = db.Column(db.String(30), nullable=False)
    dob = ''
    age = ''
    sex = db.Column(db.Enum(SexEnum), nullable=True)
    phone = ''
    state = ''
    country = ''
    nationality = ''
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now(), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', back_populates='profile')

    def __repr__(self):
        return f"{self.f_name} {self.l_name} - {self.sex}"
    
class Photo(db.Model):
    pass

