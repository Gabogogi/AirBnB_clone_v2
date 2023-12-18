#!/usr/bin/python3
# distributes an archive to your web servers, using the function do_deploy
from datetime import datetime
from fabric import ThreadingGroup as Group
from fabric import task
import os

hosts = ["54.236.46.59", "52.3.252.66"]


@task
def do_deploy(c, archive_path):
    """Deploy an archive to web servers."""
    if not os.path.isfile(archive_path):
        print("Archive does not exist")
        return False

    print("[connecting...]")
    filename = os.path.basename(archive_path)
    group = Group(*hosts, user="ubuntu")
    # Upload archive to the /tmp/ dir of remote hosts
    results = group.put(archive_path, remote=f"/tmp/{filename}")
    if results.failed:
        print("Could not push archive to remote servers")
        return False

    print("[uncompressing archive]")
    # Uncompress the archive [remote]
    # Destination filename is same as archive_path but without the extension
    fout = os.path.basename(archive_path).split(".tgz")[0]
    fout = "/data/web_static/releases/" + fout
    group.run(f"rm -rf {fout}")  # Delete the dir if it already exists
    group.run(f"mkdir -p {fout}")
    result = group.run(f"tar -xzvf /tmp/{filename} -C {fout}")
    # Delete the archive
    group.run(f"rm /tmp/{filename}")
    if results.failed:
        print("extraction failed")
        return False

    print("[creating symlink ...]")
    # Delete the symlink from the server
    group.run(f"rm -f /data/web_static/current")
    # Create a new symlink based on the extracted archive
    results = group.run(f"ln -s {fout}/web_static /data/web_static/current")

    if results.failed:
        print("Symlink creation failed")
        return False

    print("[Deployment successful]")

    return True