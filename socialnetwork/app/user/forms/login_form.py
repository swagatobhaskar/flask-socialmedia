from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired()])
    email = EmailField('Email:', validators=[Email()])
    password = PasswordField('Password:', validators=[DataRequired()])

