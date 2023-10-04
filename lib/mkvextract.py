"""Wrappers around the mkvextract command-line tool."""


import os
import subprocess
import sys


if __name__ == '__main__':
    sys.path.append(os.path.dirname(os.getcwd()))  # allow absolute imports.


from lib.data import MKVFileTrack, MKVFile


def MKVExtract(file: MKVFile, track: MKVFileTrack, output_path_base: str):
    with subprocess.Popen(['mkvextract', file.file_path, 'tracks', f'{track.track_id}:{output_path_base}']) as mkvextract_process:
        mkvextract_process.wait()
        assert mkvextract_process.returncode == 0


if __name__ == '__main__':
    from lib.mkvinfo import ReadMKVFileInfo
    f = ReadMKVFileInfo('/home/krelinga/s01e01.mkv')
    for track in filter(lambda x: x.track_type == 'subtitles', f.tracks):
        print(f'extracting track_id {track.track_id}')
        MKVExtract(f, track, track.track_id)
