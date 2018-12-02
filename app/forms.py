from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class TargetDomain(FlaskForm):
	url1 = StringField('url1', validators=[DataRequired()])
	url2 = StringField('url2', validators=[DataRequired()])

