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

from .sql import db, UserDB

class PyFlaSQL():
    """Create the application PyFlaSQL"""
    def __init__(self):
        self.myapp = self.create_app("config")  # Creating the app

        with self.myapp.app_context():
            db.create_all()
            bcrypt = Bcrypt(self.myapp)

            user = UserDB.query.filter_by(username="admin").first()
            if user is None:
                hashed_password = bcrypt.generate_password_hash("admin123")
                new_user = UserDB(username="admin", password=hashed_password, role=666)
                db.session.add(new_user)
                db.session.commit()

        # debug - print the URL map of blueprint (check the console)
        # print(self.myapp.url_map)

        self.login_manager = LoginManager()
        self.login_manager.init_app(self.myapp)
        self.login_manager.login_view = 'blueprint.login'

        @self.login_manager.user_loader
        def load_user(user_id):
            return UserDB.query.get(int(user_id))

    def create_app(self, config_path="config"):
        app = Flask(__name__)
        app.config.from_object(config_path)  # Configuring from Python Files
        app.config['UPLOAD_FOLDER'] = 'uploads'
        app.config['ALLOWED_EXTENSIONS'] = []
        
        db.init_app(app)
        from ..view.routes.blueprint import blueprint

        app.register_blueprint(blueprint, url_prefix='/')
        
        return app
