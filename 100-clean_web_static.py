#!/usr/bin/python3
# Script for deleting out-of-date archives using the function do_clean.
# This script utilizes Fabric for remote execution.
# The main function do_clean is decorated as a task for Fabric.

from datetime import datetime
from fabric import ThreadingGroup as Group
from fabric import task
import os

@task
def do_clean(c, number=0):
    """Delete out-of-date archives.

    Args:
        c (fabric.connection.Connection): The Fabric connection object.
        number (int): The number of archives to keep.
            If number is 0 or 1, keeps only the most recent archive.
            If number is 2, keeps the most and second-most recent archives, etc.
    """
    # Get a list of relative pathnames of archives.
    archives = [f"versions/{fname}" for fname in os.listdir("versions")]

    # Sort archives based on modification times (oldest to newest).
    archives = sorted(archives, reverse=False, key=lambda f: os.stat(f).st_mtime)

    # Keep the specified number of archives. Delete the rest.
    number = 1 if number == 0 else number
    for _ in range(number):
        archives.pop()

    # Delete outdated archives.
    for fname in archives:
        os.remove(fname)

