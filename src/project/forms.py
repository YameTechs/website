from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class ProjectForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    description = TextAreaField("Description")
    github_url = StringField("Github URL")
    site_url = StringField("Site URL")
    image_file = FileField("Image", validators=[FileAllowed(["jpg", "jpeg", "png"])])
    submit = SubmitField("Submit")
