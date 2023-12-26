"""Wrappers around mkvmerge command-line tool."""


import os
import subprocess


def SplitAtChapterBoundaries(file_path: str, chapter_splits: set[int],
                             output_path_pattern: str):
    chapter_splits_str = ','.join([str(x) for x in sorted(chapter_splits)])
    with subprocess.Popen(['mkvmerge', '--split',
                           f'chapters:{chapter_splits_str}', '-o',
                           output_path_pattern, file_path]) as sub:
        sub.wait()
        assert sub.returncode == 0
