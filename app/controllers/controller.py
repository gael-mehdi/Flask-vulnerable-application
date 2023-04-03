# This file is part of PyFlaSQL.
# Original author: Raphael Viera (raphael.viera@emse.fr)
# Contribution : ISMIN student X (ismin.student@etu.emse.fr)
# License: check the LICENSE file.
"""
Business logic for the main application
"""
from flask import Flask, render_template, url_for, redirect
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt

from ..models.app import PyFlaSQL
from ..models.sql import db, User
from ..models.auth import LoginForm, RegisterForm

def get_bcrypt():
    pyflasql_obj = PyFlaSQL()
    bcrypt = Bcrypt(pyflasql_obj.myapp)
    return bcrypt

def index():
    """
        Control the index page.

        Args:
            - None.

        Returns:
            - rendered index.html template
        """

    return render_template('index.html')

def login():
    """
        Control the login page.

        Args:
            - None.

        Returns:
            - rendered .html template (dashboard.html if login success or login.html if login fail)
        """
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
    """
        Control the dashboard page.
        Login is required to view this page.

        Args:
            - None.

        Returns:
            - rendered dashboard.html template
        """
    username = current_user.username
    return render_template('dashboard.html', username=username)

@login_required
def logout():
    """
        Control the logout page.
        Login is required to view this page.

        Args:
            - None.

        Returns:
            - redirect to login page
        """
    logout_user()
    return redirect(url_for('blueprint.login'))

def register():
    """
        Control the register page.

        Args:
            - None.

        Returns:
            - rendered .html template
        """
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