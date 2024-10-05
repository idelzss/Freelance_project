from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, SelectField
from wtforms.validators import DataRequired

class SubmissionForm(FlaskForm):
    description = StringField("Description", validators=[DataRequired()])
    GitHub_Url = URLField("GitHub URl(complete work send on GitHub)", validators=[DataRequired()])
    employer_id = SelectField('Select Employer Name', validators=[DataRequired()])
    submit = SubmitField("Send work")