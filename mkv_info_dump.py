#! /usr/bin/python3


from lib import constants
from lib import mkvinfo
import os

if __name__ == '__main__':
    mkv_dir = mkvinfo.ReadMKVDirectory('.')
    with open(os.path.join('.', constants.MKV_DIRECTORY_INFO_JSON), 'w') as file:
        mkv_dir.ToJson(file)
