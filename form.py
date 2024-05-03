from flask_wtf import FlaskForm 
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class MessageForm(FlaskForm):
	name = StringField('Name:', validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('Email:', validators=[DataRequired(), Email()] )
	title = StringField('Title:', validators=[DataRequired()])
	message = TextAreaField('Message:', validators=[DataRequired()])
	submit = SubmitField('Send')