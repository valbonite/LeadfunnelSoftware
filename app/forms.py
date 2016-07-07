from flask.ext.wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(Form):
	username = StringField('Username', validators=[DataRequired("Please input username")])
	password = PasswordField('Password', validators=[DataRequired("Please input password")])