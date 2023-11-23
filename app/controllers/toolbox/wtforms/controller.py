# This file is part of PyFlaSQL.
# Original author: Raphael Viera (raphael.viera@emse.fr)
# Contribution : ISMIN student X (ismin.student@etu.emse.fr)
# License: check the LICENSE file.
"""
Implements the logic for TP1 - Reconnaissance Footprint
"""
from flask import Flask, render_template, url_for, redirect, request, session, flash
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
import os
from ....models.sql import db, UserDB
from ...utils import get_shell_output, CheckIf, get_current_directory
from ....models.toolbox.forms import ToolboxUserRegForm, ToolboxUploadForm
from werkzeug.utils import secure_filename

@login_required
def toolbox_wtforms_home():
    """
        Handles the logic for /toolbox/wtforms/home
        Login is required to view this page

        Args:
            - None.

        Returns:
            - rendered template view/templates/toolbox/wtforms/home.html with the username passed as a context variable
    """
    # Get the URL path and query parameters of the current request
    # url_path = request.path

    # Do something with the URL path and query parameters
    # For example, print them to the console
    # print("URL Path:", url_path)
    username = current_user.username
    return render_template(url_for('blueprint.toolbox_wtforms_home')+'.html', username=username)

def toolbox_wtforms_user_reg_form():
    """
        Handles the logic for /toolbox/wtforms/home
        Login is required to view this page

        Args:
            - None.

        Returns:
            - rendered template view/templates/toolbox/wtforms/home.html with the username passed as a context variable
    """
    content = {"form": ToolboxUserRegForm(),
               "read_data": "empty"
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
        read_data = {"name": name,
                    "email": email,
                    "password": password,
                    "confirm_password": confirm_password,
                    "age": age,
                    "gender": gender,
                    "bio": bio,
                    "agree": agree,
                    "date": date,
                    "option": option
               }
        content["read_data"] = read_data # nested dict()

        flash('Form submitted!', 'Success')
        
    # Redirect to success page or do other logic
    return render_template(url_for('blueprint.toolbox_wtforms_user_reg_form')+'.html', content=content)

def toolbox_wtforms_upload_form():
    """
        Handles the logic for /toolbox/wtforms/upload_form
        Login is required to view this page

        Args:
            - None.

        Returns:
            - rendered template view/templates/toolbox/wtforms/upload_form.html with the username passed as a context variable
    """
    UPLOAD_FOLDER = os.path.join(get_current_directory(), "app/assets/uploads")
    content = {"form": ToolboxUploadForm(),
               "confirm": False,
               "file_path": False,
               "file_url": False,
               "filename": False
               }

    if content["form"].validate_on_submit():
        # Form has been submitted and is valid
        # Access form data using content["form"].field_name.data
        image = content["form"].image.data
        if image:
            filename = secure_filename(image.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            image.save(file_path)
            content["file_path"] = file_path
            content["filename"] = filename
            content["file_url"] = url_for('blueprint.static', filename=f'uploads/{filename}')

            # Perform further processing on the uploaded image if needed
            content["confirm"] = True
            flash('Image uploaded successfully!', 'Success')
        
        # Redirect to success page or do other logic
        return render_template(url_for('blueprint.toolbox_wtforms_upload_form')+'.html', content=content)
    return render_template(url_for('blueprint.toolbox_wtforms_upload_form')+'.html', content=content)

