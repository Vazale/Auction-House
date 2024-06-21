from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, SubmitField, IntegerField, FileField, BooleanField, validators
from wtforms.validators import length, DataRequired, equal_to, email, optional



class RegisterForm(FlaskForm):

    username = StringField(validators=[DataRequired(), length(min=8, max=12)])
    password = PasswordField(validators=[DataRequired(), length(min=8, max=64)])
    verify = PasswordField(validators=[DataRequired()])
    mail = StringField(validators=[DataRequired(), email()])
    



    

    submit = SubmitField("Register")


class LoginForm(FlaskForm):

    username = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    rem = BooleanField()

    submit = SubmitField("Login")


class ProductForm(FlaskForm):

    name = StringField(validators=[DataRequired()])
    price = IntegerField(validators=[DataRequired()])
    desc = StringField(validators=[DataRequired()])
    img = FileField(validators=[optional()])

    submit = SubmitField("Post")

