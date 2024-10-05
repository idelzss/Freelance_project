from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class ProfessionForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    description = TextAreaField("description", validators=[DataRequired()])
    submit = SubmitField("Add Profession")
