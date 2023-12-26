"""Tools for dealing with MKV chapter files."""


import re


def RenumberChapters(chapters: str) -> str:
    chapter_line_re = re.compile(r'CHAPTER(\d{2})NAME=')
    out_lines = []
    for line in chapters.splitlines():
       match = re.match(chapter_line_re, line)

       # Preserve non-matching lines
       if not match:
           out_lines.append(line)
           continue

       # Edit matching lines
       out_lines.append(f'{match.group()}Chapter {match.group(1)}')

    return '\n'.join(out_lines) + '\n'
