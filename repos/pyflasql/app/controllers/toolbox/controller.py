# This file is part of PyFlaSQL.
# Original author: Raphael Viera (raphael.viera@emse.fr)
# Contribution : ISMIN student X (ismin.student@etu.emse.fr)
# License: check the LICENSE file.
"""
Implements the logic for TP1 - Reconnaissance Footprint
"""
from flask import Flask, render_template, url_for, redirect, request
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from ...models.sql import db, UserDB
from ..utils import get_shell_output, CheckIf
from ...models.toolbox.forms import ToolboxUserRegForm


@login_required
def toolbox_home():
    """
        Handles the logic for /toolbox/home
        Login is required to view this page

        Args:
            - None.

        Returns:
            - rendered template view/templates/toolbox/home.html with the username passed as a context variable
        """
    # Get the URL path and query parameters of the current request
    # url_path = request.path

    # Do something with the URL path and query parameters
    # For example, print them to the console
    # print("URL Path:", url_path)
    username = current_user.username
    return render_template(url_for('blueprint.toolbox_home')+'.html', username=username)

def toolbox_form_example():
    content = {"form": ToolboxUserRegForm(),
               "read_data": "Waiting..."
               }
    if content["form"].validate_on_submit():
        # Form has been submitted and is valid
        # Access form data using content["form"].field_name.data
        name = content["form"].name.data
        email = content["form"].email.data
        password = content["form"].password.data
        confirm_password = content["form"].confirm_password.data
        age = content["form"].age.data
        gender = content["form"].gender.data
        bio = content["form"].bio.data
        agree = content["form"].agree.data
        date = content["form"].date.data
        option = content["form"].option.data

        # Perform desired action with form data, e.g. save to variable and show on html page
        content["read_data"] =  f"Name: {name}\n"
        content["read_data"] += f"E-mail: {email}\n"
        content["read_data"] += f"Password: {password}\n"
        content["read_data"] += f"Confirm password: {confirm_password}\n"
        content["read_data"] += f"Age: {age}\n"
        content["read_data"] += f"Gender: {gender}\n"
        content["read_data"] += f"Bio: {bio}\n"
        content["read_data"] += f"Agree: {agree}\n"
        content["read_data"] += f"Date: {date}\n"
        content["read_data"] += f"Option: {option}"
        
    # Redirect to success page or do other logic
    return render_template(url_for('blueprint.toolbox_form_example')+'.html', content=content)