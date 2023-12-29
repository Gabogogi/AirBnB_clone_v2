#!/usr/bin/python3
# Fabfile to generates a .tgz archive from the contents of web_static.
from datetime import datetime
from invoke import task
import os

@task
def do_pack(ctx):
    '''
    Generate a .tgz archive from the contents of the web_static folder.
    '''
    if os.path.isdir("versions") is False:
        if ctx.run("mkdir -p versions").failed is True:
            return None

    now = datetime.utcnow()
    ar_name = "versions/web_static_{}.tgz".format(now.strftime("%Y%m%d%H%M%S"))

    tar_command = "tar -cvzf {} web_static".format(ar_name)
    result = ctx.run(tar_command)

    if result.failed:
        return None
    else:
        return ar_name