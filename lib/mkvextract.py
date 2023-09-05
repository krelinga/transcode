"""Wrappers around the mkvextract command-line tool."""


from mkvinfo import MKVFileTrack
import os
import subprocess


def MKVExtract(track: MKVFileTrack, output_path_base: str):
    with subprocess.Popen(['mkvextract', track.mkv_file.file_path, 'tracks', f'{track.track_id}:{output_path_base}']) as mkvextract_process:
        mkvextract_process.wait()
        assert mkvextract_process.returncode == 0


if __name__ == '__main__':
    from mkvinfo import MKVFile
    f = MKVFile.from_mkv_file('/home/krelinga/s01e01.mkv')
    for track in filter(lambda x: x.track_type == 'subtitles', f.tracks):
        print(f'extracting track_id {track.track_id}')
        MKVExtract(track, track.track_id)
