from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Email, Length, EqualTo, NumberRange


class LoginForm(FlaskForm):
    email = StringField('Email: ', validators=[Email('Wrong email')])
    psw = PasswordField('Password: ', validators=[DataRequired(), Length(min=4, max=100,
                                                                         message='Password must be from 4 to 100 '
                                                                                 'symbols')])
    remember = BooleanField('Remember', default=False)
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    name = StringField('Name: ', validators=[Length(min=4, max=100, message='Name must be from 4 to 100 symbols')])
    email = StringField('Email: ', validators=[Email('Wrong email')])
    age = IntegerField('Age: ', validators=[NumberRange(min=15, max=100, message='Age must be from 15 to 100')])
    city = StringField('City: ', validators=[Length(min=4, max=100, message='City must be from 4 to 100 symbols')])
    psw = PasswordField('Password: ', validators=[DataRequired(), Length(min=4, max=100,
                                                                         message='Password must be from 4 to 100 '
                                                                                 'symbols')])
    psw2 = PasswordField('Repeat password: ',
                         validators=[DataRequired(), EqualTo('psw', message='Passwords do not equal')])
    submit = SubmitField('Register')
