from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField, URLField
from wtforms.validators import DataRequired


class ProgramForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    video_url = URLField("Video URL")
    profession = SelectField("Profession", validators=[DataRequired()])
    submit = SubmitField("Add Program")