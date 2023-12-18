#!/usr/bin/python3
# deletes out-of-date archives, using the function do_clean:
from datetime import datetime
from fabric import ThreadingGroup as Group
from fabric import task
import os


@task
def do_clean(c, number=0):
    """
    Delete out-of-date archives from the local host.
    """
    # Get list of relative pathnnames of archives.
    archives = [f"versions/{fname}" for fname in os.listdir("versions")]
    # Sort archives based on modification times (oldest to newest)
    archives = sorted(archives, reverse=False, key=lambda f: os.stat(f)[-1])

    # Keep the specified number of archives. Delete the rest.
    number = 1 if number == 0 else number
    for _ in range(number):
        archives.pop()
    for fname in archives:
        os.remove(fname)
