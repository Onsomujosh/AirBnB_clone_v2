#!/usr/bin/python3
from fabric.api import local
from time import strftime
from datetime import datetime
import os

def do_pack():
    """Creates a .tgz archive from the contents of the web_static folder."""
    
    now = datetime.now()
    formatted_time = now.strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(formatted_time)

    try:
        if not os.path.exists("versions"):
            os.makedirs("versions")

        local("tar -cvzf {} web_static".format(archive_path))
        print("web_static packed: {} -> {}Bytes".format(archive_path, os.path.getsize(archive_path)))
        return archive_path

    except Exception as e:
        return None

if __name__ == "__main__":
    result = do_pack()
    if result:
        print("New version packed: {}".format(result))
    else:
        print("Packing failed.")
