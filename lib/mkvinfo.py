"""Utility for extracting infor about MKV files."""


import json
import subprocess


class MKVFileTrack:
    def __init__(self, track_id=None):
        self.track_id = track_id

    def __repr__(self):
        return f'MKVFileTrack(track_id={self.track_id})'


class MKVFile:
    def __init__(self, file_path: str):
        self.file_path = file_path

        with subprocess.Popen(['mkvmerge', '-J', '--identify', file_path], stdout=subprocess.PIPE) as mkvmerge_process:
            json_out = mkvmerge_process.communicate()[0]
            self.json_info = json.loads(json_out)
            assert mkvmerge_process.returncode == 0

        self.tracks = []
        if self.json_info['tracks']:
            for track_json in self.json_info['tracks']:
                self.tracks.append(MKVFileTrack(track_json.get('id', None)))


if __name__ == '__main__':
    f = MKVFile('/home/krelinga/s01e01.mkv')
    print(f.file_path)
    print(f.json_info)
    print(f.tracks)
