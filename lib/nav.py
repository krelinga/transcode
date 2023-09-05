'''Peer classes to those defined in 'data' module the enable easy backward &
forward navigation between different levels of the hierarchy.'''


from __future__ import annotations
import data
from dataclasses import dataclass, field


@dataclass(frozen=True)
class _MKVFileTrack:
    data: data.MKVFileTrack
    mkv_file: _MKVFile


@dataclass(frozen=True)
class _MKVFile:
    data: data.MKVFile
    mkv_directory: _MKVDirectory
    tracks: list[_MKVFileTrack] = field(init=False)

    def __post_init__(self):
        object.__setattr__(self, 'tracks',
                [_MKVFileTrack(x, self) for x in self.data.tracks])


@dataclass(frozen=True)
class MKVDirectory:
    data: data.MKVDirectory
    files: list[_MKVFile] = field(init=False)

    def __post_init__(self):
        object.__setattr__(self, 'files',
                [_MKVFile(x, self) for x in self.data.files])


if __name__ == '__main__':
    data_track0 = data.MKVFileTrack(track_id=0)
    data_track1 = data.MKVFileTrack(track_id=1)
    data_file0 = data.MKVFile(
            file_path='/foo/0', tracks=[data_track0, data_track1])
    data_file1 = data.MKVFile(
            file_path='/foo/1', tracks=[data_track0, data_track1])
    data_directory = data.MKVDirectory(
            dir_path='/foo', files=[data_file0, data_file1])
    nav_directory = MKVDirectory(data_directory)
    print(nav_directory.data.dir_path)
    print(nav_directory.files[0].data.file_path)
    print(nav_directory.files[0].mkv_directory.data.dir_path)
    print(nav_directory)
