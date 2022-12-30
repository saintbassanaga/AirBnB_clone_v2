#!/usr/bin/python3
"""
    Fabric script that creates and distributes an archive
    on my web servers, using deploy function
"""
from fabric.api import *
from fabric.operations import run, put, sudo, local
from datetime import datetime
import os

env.hosts = ['52.91.127.212', '18.206.233.129']
created_path = None


def do_pack():
    """
        generates a .tgz archine from contents of web_static
    """
    time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    file_name = "versions/web_static_{}.tgz".format(time)
    try:
        local("sudo mkdir -p ./versions")
        local("sudo tar --create --verbose -z --file={} ./web_static"
              .format(file_name))
        return file_name
    except:
        return None


def do_deploy(archive_path):
    """
        using fabric to distribute archive
    """
    if os.path.isfile(archive_path) is False:
        return False
    try:
        archive = archive_path.split("/")[-1]
        path = "/data/web_static/releases"
        put("{}".format(archive_path), "/tmp/{}".format(archive))
        folder = archive.split(".")
        run("sudo mkdir -p {}/{}/".format(path, folder[0]))
        new_archive = '.'.join(folder)
        run("sudo tar -xzf /tmp/{} -C {}/{}/"
            .format(new_archive, path, folder[0]))
        run("sudo rm /tmp/{}".format(archive))
        run("sudo mv {}/{}/web_static/* {}/{}/"
            .format(path, folder[0], path, folder[0]))
        run("sudo rm -rf {}/{}/web_static".format(path, folder[0]))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -sf {}/{} /data/web_static/current"
            .format(path, folder[0]))
        return True
    except:
        return False


def deploy():
    """
        deploy function that creates/distributes an archive
    """
    global created_path
    if created_path is None:
        created_path = do_pack()
    if created_path is None:
        return False
    return do_deploy(created_path)
