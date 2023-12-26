"""Wrapper for mkvpropedit command."""


import subprocess


def RewriteChapters(file_path: str, chapters_file_path: str):
    with subprocess.Popen(['mkvpropedit', file_path, '-c',
                           chapters_file_path]) as sub:
        sub.wait()
        assert sub.returncode == 0
