"""Wrappers around the mkvextract command-line tool."""


from .data import MKVFileTrack, MKVFile
import os
import subprocess


def MKVExtract(file: MKVFile, track: MKVFileTrack, output_path_base: str):
    with subprocess.Popen(['mkvextract', file.file_path, 'tracks', f'{track.track_id}:{output_path_base}']) as mkvextract_process:
        mkvextract_process.wait()
        assert mkvextract_process.returncode == 0


if __name__ == '__main__':
    from mkvinfo import ReadMKVFileInfo
    f = ReadMKVFileInfo('/home/krelinga/s01e01.mkv')
    for track in filter(lambda x: x.track_type == 'subtitles', f.tracks):
        print(f'extracting track_id {track.track_id}')
        MKVExtract(f, track, track.track_id)
