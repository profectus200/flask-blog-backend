from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import Length


class AddPostForm(FlaskForm):
    title = StringField('Title: ',
                        validators=[Length(min=4, max=100, message='Title length must be from 4 to 1000 symbols')])
    text = StringField('Text: ',
                       validators=[Length(min=10, max=5000, message='Post length must be from 10 to 5000 symbols')])
    alias = StringField('Alias: ',
                        validators=[Length(min=1, max=50, message='Alias length must be from 1 to 50 symbols')])
