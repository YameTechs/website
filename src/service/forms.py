from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class ServiceForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    file = FileField(
        "File", validators=[FileAllowed(["jpg", "jpeg", "png", "pdf", "txt", "docx"])]
    )

    submit = SubmitField()
