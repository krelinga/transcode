#! /usr/bin/python3


from lib import chapters, mkvextract, mkvmerge, mkvpropedit
import os
import re
import sys
import tempfile


def main():
    assert len(sys.argv) >= 3
    to_split = sys.argv[1]
    split_points = set([int(x) for x in sys.argv[2:]])
    out_pattern = to_split.removesuffix('.mkv') + '_split_%02d.mkv'
    print(f'reading file {to_split} with split points {split_points}')

    # Do the split.
    #mkvmerge.SplitAtChapterBoundaries(to_split, split_points, out_pattern)

    # Figure out which files were created by the split.
    output_regex = re.compile(
            (os.path.basename(to_split.removesuffix('.mkv')) +
             r'_split_(\d{2}).mkv'))
    output_dir = os.path.dirname(to_split)
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


if __name__ == '__main__':
    main()
