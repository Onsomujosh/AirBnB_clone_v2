#!/usr/bin/python3
import os
from fabric.api import *

env.hosts = ['100.25.166.183', '100.25.146.150']


def do_clean(number=0):
    """Delete out-of-date archives.

    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """
    number = int(number)

    if number < 1:
        number = 1

    with lcd("versions"):
        local("ls -t | tail -n +{} | xargs rm -f".format(number + 1))

    with cd("/data/web_static/releases"):
        run("ls -t | tail -n +{} | xargs rm -rf".format(number + 1))
