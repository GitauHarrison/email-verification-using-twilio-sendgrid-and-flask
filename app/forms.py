from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email


class EmailForm(FlaskForm):
    """Emal form"""
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Send')


class VerifyForm(FlaskForm):
    """Token form"""
    token = StringField('Token', validators=[DataRequired()])
    submit = SubmitField('Verify')
