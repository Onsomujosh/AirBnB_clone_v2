#!/usr/bin/python3
import os
from fabric.api import env, local, put, run
from datetime import datetime

env.hosts = ['100.25.166.183', '100.25.146.150']


def do_pack():
    """
    Generates a tgz archive of the web_static directory
    """
    try:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = "versions/web_static_{}.tgz".format(timestamp)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(archive_name))
        return archive_name
    except:
        return None

def do_deploy(archive_path):
    """
    Distributes an archive to the web servers
    """
    if not os.path.exists(archive_path):
        return False

    try:
        archive_filename = os.path.basename(archive_path)
        archive_no_ext = os.path.splitext(archive_filename)[0]
        remote_path = "/data/web_static/releases"

        put(archive_path, "/tmp/")
        run("mkdir -p {}/{}".format(remote_path, archive_no_ext))
        run("tar -xzf /tmp/{} -C {}/{}".format(archive_filename, remote_path, archive_no_ext))
        run("rm /tmp/{}".format(archive_filename))
        run("mv {0}/{1}/web_static/* {0}/{1}/".format(remote_path, archive_no_ext))
        run("rm -rf {}/web_static".format(remote_path, archive_no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s {0}/{1}/ /data/web_static/current".format(remote_path, archive_no_ext))
        return True
    except:
        return False

def deploy():
    """
    Creates and distributes an archive to the web servers
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

if __name__ == "__main__":
    deploy()
