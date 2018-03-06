from flask_wtf import FlaskForm 
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class CatalogForm(FlaskForm):
    name= StringField('Name', validators=[DataRequired()]),
    description = FileField('Description', validators=[DataRequired()]),
    image_url = FileField('Image Upload', validators=[DataRequired()]),
    submit = SubmitField('Upload')

class CategoryForm(FlaskForm):
    name= StringField('Caption', validators=[DataRequired()])
    submit = SubmitField('Upload')
