# This file is part of PyFlaSQL.
# Original author: Raphael Viera (raphael.viera@emse.fr)
# Contribution : ISMIN student X (ismin.student@etu.emse.fr)
# License: check the LICENSE file.
"""
Business logic for the main application
"""
from flask import Flask, render_template, url_for, redirect
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt


from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

from ..models.model import db, User

def get_bcrypt():
    myapp_obj = MyApp()
    bcrypt = Bcrypt(myapp_obj.myapp)
    return bcrypt

class MyApp():
    def __init__(self):
        self.myapp = self.create_app("config")  # Creating the app
        self.test = 1

        @self.myapp.before_first_request
        def create_tables():
            db.create_all()

        print(self.myapp.url_map)

        self.login_manager = LoginManager()
        self.login_manager.init_app(self.myapp)
        self.login_manager.login_view = 'login'

        @self.login_manager.user_loader
        def load_user(user_id):
            return User.query.get(int(user_id))

    def create_app(self, config_path="config"):
        app = Flask(__name__)
        app.config.from_object(config_path)  # Configuring from Python Files

        db.init_app(app)
        from ..routes.blueprint import blueprint

        app.register_blueprint(blueprint, url_prefix='/')
        
        return app


class RegisterForm(FlaskForm):
    username = StringField(validators=[
        InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
        InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(username=username.data).first()
        if existing_user_username:
            raise ValidationError('That username already exists. Please choose a different one.')


class LoginForm(FlaskForm):
    username = StringField(validators=[
        InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "    "})

    password = PasswordField(validators=[
        InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')

def index():
    return render_template('index.html')

def login():
    bcrypt = get_bcrypt()
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('blueprint.dashboard'))
    return render_template('login.html', form=form)

@login_required
def dashboard():
    username = current_user.username
    return render_template('dashboard.html', username=username)

@login_required
def logout():
    logout_user()
    return redirect(url_for('blueprint.login'))

def register():
    bcrypt = get_bcrypt()
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        # new_user = User(username=form.username.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('blueprint.login'))

    return render_template('register.html', form=form)