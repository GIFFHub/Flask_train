from flask_wtf import  FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email


class InputForm(FlaskForm):
    name = StringField('name:', validators=[DataRequired('This field is required')])
    email = EmailField('Email Address:', validators=[Email('Invalid email address format')])
    submit = SubmitField('Send')
