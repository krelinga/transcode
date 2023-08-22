"""Utility for extracting infor about MKV files."""


import json
import subprocess


class MKVFileTrack:
    def __init__(self, track_id=None, language=None):
        self.track_id = track_id
        self.language = language

    def __repr__(self):
        return f'MKVFileTrack(track_id={self.track_id}, language={self.language})'


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
                self.tracks.append(MKVFileTrack(
                    track_id=track_json.get('id'),
                    language=track_json.get('properties', {}).get('language')))


if __name__ == '__main__':
    f = MKVFile('/home/krelinga/s01e01.mkv')
    print(f.file_path)
    print(f.json_info)
    for track in f.tracks:
        print(track)
