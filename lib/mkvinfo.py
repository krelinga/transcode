"""Utility for extracting infor about MKV files."""


import json
import subprocess


class MKVFileTrack:
    def __init__(
            self,
            mkv_file=None,
            track_id=None,
            audio_channels=None,
            default_track=None,
            forced_track=None,
            language=None,
            track_name=None,
            track_type=None):
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
            f'track_id={repr(self.track_id)}',
            f'audio_channels={repr(self.audio_channels)}',
            f'default_track={repr(self.default_track)}',
            f'forced_track={repr(self.forced_track)}',
            f'language={repr(self.language)}',
            f'track_name={repr(self.track_name)}',
            f'track_type={repr(self.track_type)}',
        ])
        return f'MKVFileTrack({parts})'


class MKVFile:
    @classmethod
    def from_mkv_file(cls, file_path: str):
        '''opens and reads the mkv file at file_path.'''
        with subprocess.Popen(['mkvmerge', '-J', '--identify', file_path], stdout=subprocess.PIPE) as mkvmerge_process:
            json_out = mkvmerge_process.communicate()[0]
            json_info = json.loads(json_out)
            assert mkvmerge_process.returncode == 0
        new_file = cls(file_path)

        if json_info['tracks']:
            for track_json in json_info['tracks']:
                new_file.add_track(
                    track_id=track_json.get('id'),
                    audio_channels=track_json.get('properties', {}).get('audio_channels'),
                    default_track=track_json.get('properties', {}).get('default_track'),
                    forced_track=track_json.get('properties', {}).get('forced_track'),
                    language=track_json.get('properties', {}).get('language'),
                    track_name=track_json.get('properties', {}).get('track_name'),
                    track_type=track_json.get('type'))

        return new_file

    def __repr__(self):
        # TODO: fix this to use a builder pattern or something?
        return f'MKVFile({repr(self.file_path)})'

    def __init__(self, file_path):
        self.file_path = file_path
        self.tracks = []

    def add_track(self, **kwargs):
        '''Creates a new MKVFileTrack and adds to this MKVFile.

        Accepts all args supported by the MKVFileTrack constructor, except for
        mkv_file.'''
        assert 'mkv_file' not in kwargs
        self.tracks.append(MKVFileTrack(mkv_file=self, **kwargs))


if __name__ == '__main__':
    f = MKVFile.from_mkv_file('/home/krelinga/s01e01.mkv')
    for track in f.tracks:
        print(track)
