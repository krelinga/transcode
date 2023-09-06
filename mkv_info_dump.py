#! /usr/bin/python3


from lib import constants
from lib import mkvinfo
import os

def main():
    mkv_dir = mkvinfo.ReadMKVDirectory('.')
    if len(mkv_dir.files) == 0:
        return
    with open(os.path.join('.', constants.MKV_DIRECTORY_INFO_JSON), 'w') as file:
        mkv_dir.ToJson(file)

if __name__ == '__main__':
    main()
