#! /usr/bin/python3

import getpass
from lib import chapters, filesystem, mkvextract, mkvmerge, mkvpropedit
import os
import re
import sys
import tempfile


def main():
    assert len(sys.argv) >= 3
    to_split = sys.argv[1]
    output_dir = os.path.dirname(to_split)

    # Make sure the path is owned by the right owner.
    current_user = getpass.getuser()
    filesystem.RecursivelyChangeOwner(output_dir, current_user)
    print(f'ensured that {output_dir} is owned by {current_user}')

    # Do the split.
    split_points = set([int(x) for x in sys.argv[2:]])
    out_pattern = to_split.removesuffix('.mkv') + '_split_%02d.mkv'
    print(f'reading file {to_split} with split points {split_points}')
    mkvmerge.SplitAtChapterBoundaries(to_split, split_points, out_pattern)

    # Figure out which files were created by the split.
    output_regex = re.compile(
            (os.path.basename(to_split.removesuffix('.mkv')) +
             r'_split_(\d{2}).mkv'))
    output_paths = []
    for file_name in sorted(os.listdir(output_dir)):
        if re.fullmatch(output_regex, file_name):
            output_paths.append(os.path.join(output_dir, file_name))

    with tempfile.TemporaryDirectory() as temp_dir:
        for file_path in output_paths:
            chapter_path = os.path.join(temp_dir, os.path.basename(file_path))
            # Extract exiting chapters from current file.
            mkvextract.ExtractChapters(file_path, chapter_path)

            # Rewrite existing chapters in temporary file.
            with open(chapter_path, 'r+') as chapter_file:
                chapter_info = chapter_file.read()
                rewritten_chapter_info = chapters.RenumberChapters(chapter_info)
                chapter_file.seek(0)
                chapter_file.write(rewritten_chapter_info)
                chapter_file.truncate()

            # Apply new chapters.
            mkvpropedit.RewriteChapters(file_path, chapter_path)

            print(f'renumbered chapters for {file_path}')

    # Rename unsplit file.
    unsplit_path = os.path.join(
            output_dir,
            os.path.basename(to_split).removesuffix('.mkv') + '_unsplit.mkv')
    os.rename(to_split, unsplit_path)
    print(f'renamed {to_split} to {unsplit_path}')


if __name__ == '__main__':
    main()
