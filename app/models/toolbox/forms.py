from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField, TextAreaField, RadioField
from wtforms.validators import DataRequired, Email, InputRequired, Length, ValidationError, NumberRange, URL, EqualTo
from wtforms.fields import DateField
from ..sql import db, UserDB


class ToolboxUserRegForm(FlaskForm):
    name = StringField('Name', validators=[
        InputRequired(), Length(min=2, max=50)], render_kw={"placeholder": "Name"})
    
    email = StringField('Email', validators=[
        Email(), InputRequired(), Length(max=120)], render_kw={"placeholder": "Email"})
    
    password = PasswordField('Password', validators=[
        InputRequired(), Length(min=8)], render_kw={"placeholder": "Password"})
    
    confirm_password = PasswordField('Confirm Password', validators=[
        EqualTo('password', message='Passwords must match')], render_kw={"placeholder": "Confirm Password"})
    
    age = IntegerField('Age', validators=[
        NumberRange(min=18, max=99)], render_kw={"placeholder": "Age"})
    
    gender = SelectField('Gender', choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    
    bio = TextAreaField('Bio', validators=[
        Length(max=500)], render_kw={"placeholder": "Bio"})
    
    agree = BooleanField('I Agree', validators=[DataRequired()])
    
    option = RadioField('Option', choices=[('A', 'Option A'), ('B', 'Option B'), ('C', 'Option C')])

    date = DateField('Date', validators=[
        InputRequired()], format='%Y-%m-%d', render_kw={"placeholder": "Date"})
    
    submit = SubmitField('Submit')


class ToolboxUploadForm(FlaskForm):
    image = FileField('Image', validators=[
        InputRequired(), 
        FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Only JPEG, PNG, and GIF images are allowed.')])
    submit = SubmitField('Upload')


class ToolboxBookLibrary(FlaskForm):
    title = StringField('Book Title', validators=[
        InputRequired(), Length(min=2, max=200)], render_kw={"placeholder": "Title"})
    
    author = StringField('Author', validators=[
        InputRequired(), Length(min=2, max=200)], render_kw={"placeholder": "Author"})
    
    cover = FileField('Cover', validators=[
        FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Only JPEG, PNG, and GIF images are allowed.')])
    
    description = TextAreaField('Description', validators=[
        Length(max=500)], render_kw={"placeholder": "Description"})
    
    submit = SubmitField('Submit')