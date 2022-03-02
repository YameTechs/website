from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField, SubmitField
from wtforms.validators import EqualTo, Length, ValidationError


class EditUserDataForm(FlaskForm):
    username = StringField(validators=[Length(min=3, max=25)])
    email = EmailField()
    password = PasswordField()
    submit = SubmitField()


class ResendEmailButton(FlaskForm):
    submit = SubmitField("Send Verification Email")
