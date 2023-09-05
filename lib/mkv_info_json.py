'''Functions for reading & writing .mkvinfo.json files.'''


import json
import os


def __GetMkvInfoPath(dirpath: str):
    '''Given a directory path, return the path to the corresponding .mkvinfo.json file.'''
    return os.path.join(dirpath, '.mkvinfo.json')


def WriteMkvInfoJson(dirpath: str):
    '''Writes a .mkvinfo.json file in dirpath.'''
    with open(__GetMkvInfoPath(dirpath), 'w') as mkvinfofile:
        json.dump(
                {'test_key1': 'test_value1', 'test_key2': 'test_value2'},
                mkvinfofile,
                indent='\t',
                sort_keys=True)


def ReadMkvInfoJson(dirpath: str):
    '''Reads a .mkvinfo.json file from dirpath.'''
    with open(__GetMkvInfoPath(dirpath), 'r') as mkvinfofile:
        print(json.load(mkvinfofile))


if __name__ == '__main__':
    print(__GetMkvInfoPath('/some/path'))
    import tempfile
    with tempfile.TemporaryDirectory() as temp_dir:
        WriteMkvInfoJson(temp_dir)
        with open(__GetMkvInfoPath(temp_dir), 'r') as mkvinfofile:
            print(mkvinfofile.read())
        ReadMkvInfoJson(temp_dir)
