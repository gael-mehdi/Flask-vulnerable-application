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
from ....models.sql import db, UserDB, ToolboxBookLibraryDB
from ...utils import get_shell_output, CheckIf, get_current_directory
from ....models.toolbox.forms import ToolboxBookLibrary
from werkzeug.utils import secure_filename


@login_required
def toolbox_database_home():
    """
        Handles the logic for /toolbox/database/home
        Login is required to view this page

        Args:
            - None.

        Returns:
            - rendered template view/templates/toolbox/database/home.html with the username passed as a context variable
    """
    # Get the URL path and query parameters of the current request
    # url_path = request.path

    # Do something with the URL path and query parameters
    # For example, print them to the console
    # print("URL Path:", url_path)
    username = current_user.username
    return render_template(url_for('blueprint.toolbox_database_home')+'.html', username=username)

def toolbox_database_insert_data():
    """
        Handles the logic for /toolbox/wtforms/home
        Login is required to view this page

        Args:
            - None.

        Returns:
            - rendered template view/templates/toolbox/database/toolbox_database_insert_data.html with the username passed as a context variable
    """
    UPLOAD_FOLDER = os.path.join(get_current_directory(), "app/assets/uploads")

    content = {"form": ToolboxBookLibrary(),
               "read_data": False,
               "is_insert":False,
               "is_remove":False
               }
    
    # INSERT SECTION
    if content["form"].validate_on_submit() and not 'remove' in request.form:
        # Form has been submitted and is valid
        # Access form data using content["form"].field_name.data
        title = content["form"].title.data
        author = content["form"].author.data
        description = content["form"].description.data
        cover = content["form"].cover.data

        if cover:
            filename = secure_filename(cover.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            cover.save(file_path)
        else:
            filename = "no_cover.png"

        db.session.add(ToolboxBookLibraryDB(title=title, 
                                            author=author, 
                                            description=description, 
                                            cover=filename))
        db.session.commit()

        flash('Book added to the database!', 'Success')
    
    # REMOVE SECTION
    if request.method == 'POST' and 'remove' in request.form:
        # Get the book ID from the form
        book_id = request.form['remove']
        # Query the database to get the book with the specified ID
        book = ToolboxBookLibraryDB.query.get(book_id)
        if book:
            # Delete the book from the database
            db.session.delete(book)
            db.session.commit()

            if "no_cover.png" not in book.cover:
                os.remove(os.path.join(UPLOAD_FOLDER, book.cover))
                
            flash('Book removed from the database!', 'Success')


    books = ToolboxBookLibraryDB.query.all()
    # Perform desired action with form data, e.g. save to variable and show on html page
    read_data = {"books": books,
                 "n_books": len(books),
                 "covers_url": url_for('blueprint.static', filename='uploads/')
                }
    
    content["read_data"] = read_data # nested dict()

    

    # Redirect to success page or do other logic
    return render_template(url_for('blueprint.toolbox_database_insert_data')+'.html', content=content)

