#!/usr/bin/python3
# Fabfile to generates a .tgz archive from the contents of web_static.
from datetime import datetime
from fabric import task
import os


@task
def do_pack(ctx):
    """Compress the pwd into an archive in the versions"""
    print("Hello world")
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    dt = datetime.now()
    archive_name = f"web_static_{dt.year}{dt.month}{dt.day}{dt.hour}"\
                   f"{dt.minute}{dt.second}.tgz"
    print(archive_name)
    excludes = "--exclude=versions --exclude=.git --exclude=.gitignore"
    # Compress all files in the pwd to the versions/ dir.
    result = ctx.run(f"tar {excludes} -czvf versions/{archive_name} .")
    if not result.ok:
        return False

    return "versions/" + archive_name 
