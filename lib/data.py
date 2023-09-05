'''Data Classes for objects known to this system.'''


# Necessary to emulate hoisting in type hints.
from __future__ import annotations

import copy
from dataclasses import asdict, dataclass, field, fields


def _FromDictHelper(_cls, _d: dict, **overrides):
    _d = copy.copy(_d)  # Make it safe to remove elements.
    new_values = {}
    for f in fields(_cls):
        if f.name not in _d: continue
        if f.name in overrides:
            new_values[f.name] = overrides[f.name](_d[f.name])
        else:
            new_values[f.name] = _d[f.name]
    return _cls(**new_values)


@dataclass(frozen=True)
class MKVFileTrack:
    track_id: int
    audio_channels: int = field(default=None)
    default_track: bool = field(default=None)
    forced_track: bool = field(default=None)
    language: str = field(default=None)
    track_name: str = field(default=None)
    track_type: str = field(default=None)

    @classmethod
    def FromDict(cls, d: dict) -> MKVFileTrack:
        return _FromDictHelper(cls, d)


@dataclass(frozen=True)
class MKVFile:
    file_path: str
    tracks: list[MKVFileTrack] = field(default_factory=lambda: [])

    @classmethod
    def FromDict(cls, d: dict) -> MKVFile:
        return _FromDictHelper(
                cls,
                d,
                tracks = lambda x: [MKVFileTrack.FromDict(t) for t in x])

@dataclass(frozen=True)
class MKVDirectory:
    dir_path: str
    files: list[MKVFile] = field(default_factory=lambda: [])

    @classmethod
    def FromDict(cls, d: dict) -> MKVDirectory:
        return _FromDictHelper(
                cls,
                d,
                files=lambda files: [MKVFile.FromDict(file) for file in files])


if __name__ == '__main__':
    track = MKVFileTrack(track_id=0, audio_channels=1, language='english')
    file = MKVFile(file_path='/foo/bar', tracks=[track])
    directory = MKVDirectory(dir_path='/foo', files=[file])
    print(directory)
    print(file)
    print(track)
    dir_as_dict = asdict(directory)
    print(dir_as_dict)
    print(MKVDirectory.FromDict(dir_as_dict))
