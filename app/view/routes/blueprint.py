# This file is part of PyFlaSQL.
# Original author: Raphael Viera (raphael.viera@emse.fr)
# Contribution : ISMIN student X (ismin.student@etu.emse.fr)
# License: check the LICENSE file.
"""
Configures the address paths (URL routes)
"""
from flask import Blueprint
from ...controllers.controller import index, login, register, dashboard, logout
from ...controllers.srie.tp1_recon_footprint.controller import srie_tp1_recon_footprint, srie_tp1_pingaddr, srie_tp1_ipaddr
from ...controllers.srie.tp2_scanning_networks.controller import srie_tp2_scanning_networks
from ...controllers.srie.tp3_enumeration.controller import srie_tp3_enumeration
from ...controllers.srie.tp4_gaining_access.controller import srie_tp4_gaining_access
from ...controllers.user_profile.controller import user_profile

blueprint = Blueprint('blueprint', __name__, template_folder='../templates', static_folder='../templates/styles')

# Home
blueprint.route('/')(index)
blueprint.route('/login', methods=['GET', 'POST'])(login)
blueprint.route('/register', methods=['GET', 'POST'])(register)
blueprint.route('/dashboard', methods=['GET', 'POST'])(dashboard)
blueprint.route('/logout', methods=['GET', 'POST'])(logout)

# User Profile
blueprint.route('/user_profile/user_profile', methods=['GET', 'POST'])(user_profile)

# TP1 - Reconnaissance / Footprint
blueprint.route('/srie/tp1_recon_footprint/home', methods=['GET', 'POST'])(srie_tp1_recon_footprint)
blueprint.route('/srie/tp1_recon_footprint/pingaddr', methods=['GET', 'POST'])(srie_tp1_pingaddr)
blueprint.route('/srie/tp1_recon_footprint/ipaddr', methods=['GET', 'POST'])(srie_tp1_ipaddr)

# TP2 - Scanning Networks
blueprint.route('/srie/tp2_scanning_networks/home', methods=['GET', 'POST'])(srie_tp2_scanning_networks)

# TP3 - Enumeration
blueprint.route('/srie/tp3_enumeration/home', methods=['GET', 'POST'])(srie_tp3_enumeration)

# TP4 - Gaining Access
blueprint.route('/srie/tp4_gaining_access/home', methods=['GET', 'POST'])(srie_tp4_gaining_access)
