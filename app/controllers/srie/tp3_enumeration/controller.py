# This file is part of PyFlaSQL.
# Original author: Raphael Viera (raphael.viera@emse.fr)
# Contribution : ISMIN student X (ismin.student@etu.emse.fr)
# License: check the LICENSE file.
"""
Implements the logic for TP3 - Enumeration
"""
from flask import Flask, render_template, url_for, redirect
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from ....models.sql import db, User
from ...utils import get_shell_output
from ....models.srie.tp1_recon_footprint.forms import PingAddrForm


@login_required
def srie_tp3_enumeration():
    """
        Logic for /srie/tp3_enumeration/home
        Login is required to view this page

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp3_enumeration/home.html
        """
    username = current_user.username
    return render_template(url_for('blueprint.srie_tp3_enumeration')+'.html', username=username)