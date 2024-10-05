from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired


class NotAcceptForm(FlaskForm):
    description = TextAreaField("Write the corrections that should be made", validators=[DataRequired()])
    submit = SubmitField("Send")