'''Functions for reading & writing .mkvinfo.json files.'''


from collections.abc import Sequence
import json
import mkvinfo
import os


def __GetMkvInfoPath(dirpath: str):
    '''Given a directory path, return the path to the corresponding .mkvinfo.json file.'''
    return os.path.join(dirpath, '.mkvinfo.json')


def WriteMkvInfoJson(dirpath: str, mkv_files: Sequence[mkvinfo.MKVFile]) -> None:
    '''Writes a .mkvinfo.json file in dirpath.'''
    d = {
            'files': [
                {
                    'file_path': x.file_path,
                } for x in mkv_files],
        }
    with open(__GetMkvInfoPath(dirpath), 'w') as mkvinfofile:
        json.dump(d, mkvinfofile, indent='\t', sort_keys=True)


def ReadMkvInfoJson(dirpath: str):
    '''Reads a .mkvinfo.json file from dirpath.'''
    with open(__GetMkvInfoPath(dirpath), 'r') as mkvinfofile:
        print(json.load(mkvinfofile))


if __name__ == '__main__':
    print(__GetMkvInfoPath('/some/path'))
    import tempfile
    with tempfile.TemporaryDirectory() as temp_dir:
        WriteMkvInfoJson(
                temp_dir,
                [mkvinfo.MKVFile('/foo/bar'), mkvinfo.MKVFile('/foo/baz')])
        with open(__GetMkvInfoPath(temp_dir), 'r') as mkvinfofile:
            print(mkvinfofile.read())
        ReadMkvInfoJson(temp_dir)
