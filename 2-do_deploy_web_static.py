#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers"""

from os import path
from fabric.api import put, run, env

env.hosts = ['35.231.103.25', '35.190.157.5']


def do_deploy(archive_path):
    """func to deploy archive"""
    if not path.exists(archive_path):
        return False
    try:
        #Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp/')
        #getting file name
        file_name = archive_path.split("/")[-1]
        folder_name = file_name.split(".")[0]
        #Uncompress the archive
        run('mkdir -p /data/web_static/releases/' + folder_name + '/')
        run('tar -xzf /tmp/' + file_name +
            '-C /data/web_static/releases/' + folder_name + '/'
        #Delete the archive and the symbolic link
        run('rm /tmp/' + file_name)
        run('rm -rf /data/web_static/releases/'
            + folder_name + '/web_static')
        run('rm -rf /data/web_static/current')
        #Create a new the symbolic link
        run('ln -sf /data/web_static/releases/'
            + folder_name + '/ /data/web_static/current')
        return True
    except:
        return False
