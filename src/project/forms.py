from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class ProjectForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=25)])
    description = TextAreaField("Description", validators=[Length(max=50)])
    github_url = StringField("Github URL", validators=[Length(max=50)])
    site_url = StringField("Site URL", validators=[Length(max=50)])
    image_file = FileField("Image", validators=[FileAllowed(["jpg", "jpeg", "png"])])
    submit = SubmitField("Submit")
