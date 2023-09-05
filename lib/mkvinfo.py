"""Utility for extracting infor about MKV files."""


from data import MKVFileTrack, MKVFile
import json
import subprocess


def ReadMKVFileInfo(file_path: str) -> MKVFile:
    '''opens and reads the mkv file at file_path.'''
    with subprocess.Popen(
            ['mkvmerge', '-J', '--identify', file_path],
            stdout=subprocess.PIPE) as mkvmerge_process:
        json_out = mkvmerge_process.communicate()[0]
        json_info = json.loads(json_out)
        assert mkvmerge_process.returncode == 0

    class Getter:
        def __init__(self, d: dict):
            self.__d = d

        def __call__(self, *path_parts):
            current = self.__d
            for part in path_parts:
                if part not in current: return None
                current = current[part]
            return current

    tracks = []
    if json_info['tracks']:
        for track_json in json_info['tracks']:
            get = Getter(track_json)
            tracks.append(MKVFileTrack(
                track_id=get('id'),
                audio_channels=get('properties', 'audio_channels'),
                default_track=get('properties', 'default_track'),
                forced_track=get('properties', 'forced_track'),
                language=get('properties', 'language'),
                track_name=get('properties', 'track_name'),
                track_type=get('type')))

    return MKVFile(file_path=file_path, tracks=tracks)


if __name__ == '__main__':
    f = ReadMKVFileInfo('/home/krelinga/s01e01.mkv')
    for track in f.tracks:
        print(track)
