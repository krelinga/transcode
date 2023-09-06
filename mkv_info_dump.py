#! /usr/bin/python3


from lib import mkvinfo

if __name__ == '__main__':
    for file in mkvinfo.ReadMKVDirectory('.').files:
        print(file)
