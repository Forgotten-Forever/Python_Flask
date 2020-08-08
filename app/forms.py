"""
                                _ooOoo_
                               o8888888o
                               88" . "88
                               (| -_- |)
                               O\  =  /O
                            ____/`---'\____
                          .'  \\|     |//  `.
                         /  \\|||  :  |||//  \
                        /  _||||| -:- |||||-  \
                        |   | \\\  -  /// |   |
                        | \_|  ''\---/''  |   |
                        \  .-\__  `-`  ___/-. /
                      ___`. .'  /--.--\  `. . __
                   ."" '<  `.___\_<|>_/___.'  >'"".
                  | | :  `- \`.;`\ _ /`;.`/ - ` : | |
                  \  \ `-.   \_ __\ /__ _/   .-` /  /
             ======`-.____`-.___\_____/___.-`____.-'======
                                `=---='
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                       佛祖保佑        永无BUG
"""
from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from app.models import User


class RegisterForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=6, max=20)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
	confirm = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
	# recaptcha = RecaptchaField()
	submit = SubmitField('Register')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('Username already token, please choose another one.')

	def validate_email(self, email):
		email = User.query.filter_by(email=email.data).first()
		if email:
			raise ValidationError('Email already token, please choose another one.')


class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=6, max=20)])
	password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
	remember = BooleanField('Remember')
	submit = SubmitField('Sign In')


class PasswordResetRequestForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	submit = SubmitField('Send')

	def validate_email(self, email):
		email = User.query.filter_by(email=email.data).first()
		if not email:
			raise ValidationError('Email not exists.')


class ResetPasswordForm(FlaskForm):
	password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
	confirm = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('ResetPassword')


class PortTweetForm(FlaskForm):
	text = TextAreaField('Say Something  ....', validators=[DataRequired(), Length(min=1, max=40)])
	submit = SubmitField('Post Text')


class UploadPhotoForm(FlaskForm):
	photo =FileField(validators=[FileRequired()])
	submit = SubmitField('Upload')