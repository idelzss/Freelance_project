from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired


class JobForm(FlaskForm):
    title = StringField("Job Title", validators=[DataRequired()])
    description = TextAreaField("Job Description", validators=[DataRequired()])
    profession = SelectField("Profession", coerce=int, validators=[DataRequired()])
    submit = SubmitField("Create Job")