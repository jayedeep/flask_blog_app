from wtforms import StringField,PasswordField,SubmitField,BooleanField,ValidationError,TextAreaField
from wtforms.validators import DataRequired,Length,Email,EqualTo
from flaskblog.models import User
from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed



class RegistrationForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Sign Up')

    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("This Username is token,Please Choose Different One!")

    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("This Email is token,Please Choose Different One!")


class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    remember=BooleanField('Remember Me')
    submit=SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
    email=StringField('Email',validators=[DataRequired(),Email()])
    picture =FileField("Update Profile Picture",validators=[FileAllowed(['jpg','png'])])
    submit=SubmitField('Update')

    def validate_username(self,username):
        if username.data != current_user.username:
            user=User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError("This Username is token,Please Choose Different One!")

    def validate_email(self,email):
        if email.data != current_user.email:

            user=User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("This Email is token,Please Choose Different One!")

class RequestResetForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    submit=SubmitField('Request Password Reset')

    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError("There is no any Account with this Email,You must register first")

class ResetPasswordForm(FlaskForm):
    password=PasswordField('Password',validators=[DataRequired()])
    confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Reset Password')