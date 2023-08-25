"""Utility for extracting infor about MKV files."""


import json
import subprocess


class MKVFileTrack:
    def __init__(self, mkv_file=None, track_id=None, audio_channels=None, default_track=None, forced_track=None, language=None, track_name=None, track_type=None):
        self.mkv_file = mkv_file
        self.track_id = track_id
        self.audio_channels = audio_channels
        self.default_track = default_track
        self.forced_track=forced_track
        self.language = language
        self.track_name = track_name
        self.track_type = track_type

    def __repr__(self):
        parts = ', '.join([
            f'mkv_file={repr(self.mkv_file)}',
            f'track_id={self.track_id}',
            f'audio_channels={self.audio_channels}',
            f'default_track={self.default_track}',
            f'forced_track={self.forced_track}',
            f'language={self.language}',
            f'track_name={self.track_name}',
            f'track_type={self.track_type}',
        ])
        return f'MKVFileTrack({parts})'


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
                self.tracks.append(MKVFileTrack(self,
                    track_id=track_json.get('id'),
                    audio_channels=track_json.get('properties', {}).get('audio_channels'),
                    default_track=track_json.get('properties', {}).get('default_track'),
                    forced_track=track_json.get('properties', {}).get('forced_track'),
                    language=track_json.get('properties', {}).get('language'),
                    track_name=track_json.get('properties', {}).get('track_name'),
                    track_type=track_json.get('type')))

    def __repr__(self):
        return f"MKVFile('{self.file_path}')"


if __name__ == '__main__':
    f = MKVFile('/home/krelinga/s01e01.mkv')
    for track in f.tracks:
        print(track)
