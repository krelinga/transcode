'''Functions for reading & writing .mkvinfo.json files.'''


import os


def GetMkvInfoPath(dirpath: str):
    '''Given a directory path, return the path to the corresponding .mkvinfo.json file.'''
    return os.path.join(dirpath, '.mkvinfo.json')





if __name__ == '__main__':
    print(GetMkvInfoPath('/some/path'))
