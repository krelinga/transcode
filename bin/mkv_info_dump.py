#! /usr/bin/python3


import lib.mkvinfo

if __name__ == '__main__':
    for file in mkvinfo.ReadMKVDirectory('.').files:
        print(file)
