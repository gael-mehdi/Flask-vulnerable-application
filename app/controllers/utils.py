# This file is part of PyFlaSQL.
# Original author: Raphael Viera (raphael.viera@emse.fr)
# Contribution : ISMIN student X (ismin.student@etu.emse.fr)
# License: check the LICENSE file.
"""
Implement reusable functions
"""
import subprocess as sp

def get_shell_output(call_string):
    output = sp.getoutput(call_string)
    return output