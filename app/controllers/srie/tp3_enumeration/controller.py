# This file is part of PyFlaSQL.
# Original author: Raphael Viera (raphael.viera@emse.fr)
# Contribution : ISMIN student X (ismin.student@etu.emse.fr)
# License: check the LICENSE file.
"""
Business logic for enumeration
"""
from flask import Flask, render_template, url_for, redirect
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt


from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from ....models.model import db, User
from ...utils import get_shell_output


class PingAddrForm(FlaskForm):
    ip_address = StringField(validators=[
        InputRequired(), Length(min=2, max=50)], render_kw={"placeholder": "ip_address"})

    submit = SubmitField('Ping')

class WhoisForm(FlaskForm):
    whois_addr = StringField(validators=[
        InputRequired(), Length(min=2, max=100)], render_kw={"placeholder": "whois_addr"})

    submit = SubmitField('WHOIS')


@login_required
def srie_tp3_enumeration():
    username = current_user.username
    # return render_template('dashboard.html', username=username)
    return render_template(url_for('blueprint.srie_tp3_enumeration')+'.html', username=username)


@login_required
def srie_tp1_pingaddr():
    form = PingAddrForm()
    if form.validate_on_submit():
        ip_address = form.ip_address.data
        print(ip_address)
    return render_template(url_for('blueprint.srie_tp1_pingaddr')+'.html', form=form)

    