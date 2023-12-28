"""Utilities for manipulating the filesystem."""


from pathlib import Path
import subprocess


def RecursivelyChangeOwner(dir_path: str, new_owner: str):
    path = Path(dir_path)
    try:
        current_owner = path.owner()
    except KeyError:
        current_owner = None
    if current_owner == new_owner: return

    with subprocess.Popen(['sudo', 'chown', '-R', new_owner, dir_path]) as sub:
        sub.wait()
        assert sub.returncode == 0
