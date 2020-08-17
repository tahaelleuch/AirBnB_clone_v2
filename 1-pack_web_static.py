#!/usr/bin/python3
"""tgz with fabric"""

from datetime import datetime
from fabric.api import *
from os import path

def do_pack():
    """do_pack function"""
    local("mkdir -p versions")
    file = "versions/web_static_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".tgz"
    local("tar -cvzf " + file + " web_static")
    if path.exists(file):
        return file
    else:
        return None
