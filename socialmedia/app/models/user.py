import enum
from datetime import datetime, timedelta
from sqlalchemy import event
from sqlalchemy.sql import func

from .extensions import db


class SexEnum(enum.Enum):
    male = 'Male'
    female = 'Female'
    other = 'Other'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(30), nullable=False)
    l_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    sex = db.Column(db.Enum(SexEnum), nullable=True)
    subscription = db.relationship('Subscription', uselist=False, back_populates='user')

    def __repr__(self):
        return f"{self.f_name} {self.l_name} - {self.sex}"
    
class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=False)
    date_updated = db.Column(db.DateTime(timezone=True), onupdate=func.now(), nullable=True)
    valid_upto = db.Column(db.DateTime(timezone=True), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', back_populates='subscription')

    def __repr__(self):
        return f"User: {self.user_id} | Date created: {self.date_created} | Valid Upto: {self.valid_upto} "
