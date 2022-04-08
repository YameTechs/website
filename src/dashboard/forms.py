# from flask_wtf.file import FileAllowed, FileField
from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

from src.models import User


class UpdateAccountForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=3, max=30)]
    )

    email = EmailField("Email", validators=[DataRequired()])
    # picture = FileField(
    #     "Update Profile Picture", validators=[FileAllowed(["jpeg", "jpg", "png"])]
    # )
    submit = SubmitField("Update")

    def validate_username(self, username):
        if username.data == current_user.username:
            return

        user = User.query.filter_by(username=username.data).first()

        if user is None:
            return

        raise ValidationError("Username is taken. Please take another one")

    def validate_email(self, email):
        if email.data == current_user.email:
            return

        user = User.query.filter_by(email=email.data).first()

        if user is None:
            return

        raise ValidationError("Email is taken. No alts allowed")


class ResendEmailButton(FlaskForm):
    submit = SubmitField("Verify my account!")
