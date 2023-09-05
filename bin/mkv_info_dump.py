#! /usr/bin/python3


import os


def __raise(e: Exception):
    '''Only necessary because lambda expressions can't raise exceptions.'''
    raise e


def list_mkv_paths():
    '''Returns a list of .mkv file paths relative to the current directory.'''
    mkv_file_list = []
    for root, dirs, files in os.walk('.', onerror=__raise, followlinks=True):
        for mkv_file in filter(lambda x: x.endswith('.mkv'), files):
            mkv_file_list.append(os.path.join(root, mkv_file))
    return mkv_file_list


if __name__ == '__main__':
    for mkv_path in list_mkv_paths():
        print(mkv_path)
