# This file is part of PyFlaSQL.
# Original author: Raphael Viera (raphael.viera@emse.fr)
# Contribution : ISMIN student X (ismin.student@etu.emse.fr)
# License: check the LICENSE file.
"""
Implements the logic for TP1 - Reconnaissance Footprint
"""
from flask import Flask, render_template, url_for, redirect
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from ....models.sql import db, UserDB
from ...utils import get_shell_output, CheckIf
from ....models.srie.tp1_recon_footprint.forms import PingAddrForm


@login_required
def srie_home():
    """
        Handles the logic for /srie/home
        Login is required to view this page

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/home.html with the username passed as a context variable
        """
    username = current_user.username
    return render_template(url_for('blueprint.srie_home')+'.html', username=username)

@login_required
def srie_tp1_recon_footprint():
    """
        Handles the logic for /srie/tp1_recon_footprint/home
        Login is required to view this page

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp1_recon_footprint/home.html with the username passed as a context variable
        """
    username = current_user.username
    return render_template(url_for('blueprint.srie_tp1_recon_footprint')+'.html', username=username)

@login_required
def srie_tp1_ipaddr():
    """
        Handles the logic for view/templates/srie/tp1_recon_footprint/ipaddr.html
        Login is required to view this page

        Print in the user interface private and public IP addresses.

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp1_recon_footprint/ipaddr.html with content passed as a context variable
        """
    # Create a dictionary to store the private and public IP addresses
    content = {"ip_address_private": "x.x.x.x", 
               "ip_address_public": "x.x.x.x",
               "cmd_ip_address_private": f"hostname -I",
               "cmd_ip_address_public": f"To be implemented"
               }
    # Uses get_shell_output() to execute a command in the shell and store the output in the dict.
    content["ip_address_private"] = get_shell_output(content["cmd_ip_address_private"])
    content["ip_address_public"] = "To be implemented"
    return render_template(url_for('blueprint.srie_tp1_ipaddr')+'.html', content=content)



