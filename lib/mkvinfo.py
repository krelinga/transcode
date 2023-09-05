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

    tracks = []
    if json_info['tracks']:
        for track_json in json_info['tracks']:
            tracks.append(MKVFileTrack(
                track_id=track_json.get('id'),
                audio_channels=track_json.get('properties', {}).get('audio_channels'),
                default_track=track_json.get('properties', {}).get('default_track'),
                forced_track=track_json.get('properties', {}).get('forced_track'),
                language=track_json.get('properties', {}).get('language'),
                track_name=track_json.get('properties', {}).get('track_name'),
                track_type=track_json.get('type')))

    return MKVFile(file_path=file_path, tracks=tracks)


if __name__ == '__main__':
    f = ReadMKVFileInfo('/home/krelinga/s01e01.mkv')
    for track in f.tracks:
        print(track)
