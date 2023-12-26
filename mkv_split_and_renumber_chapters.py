#! /usr/bin/python3


from lib import mkvmerge
import sys


def main():
    assert len(sys.argv) >= 3
    to_split = sys.argv[1]
    split_points = set([int(x) for x in sys.argv[2:]])
    out_pattern = to_split.removesuffix('.mkv') + '_split_%02d.mkv'
    print(f'reading file {to_split} with split points {split_points}')

    mkvmerge.SplitAtChapterBoundaries(to_split, split_points, out_pattern)


if __name__ == '__main__':
    main()
