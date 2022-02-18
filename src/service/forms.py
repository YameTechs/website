from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import IntegerField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class ServiceForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    price = IntegerField("Price", validators=[DataRequired()])
    image_file = FileField("Image", validators=[FileAllowed(["jpg", "jpeg", "png"])])
    submit = SubmitField()
