'''Data Classes for objects known to this system.'''


# Necessary to emulate hoisting in type hints.
from __future__ import annotations

import copy
from dataclasses import asdict, dataclass, field, fields
import json


def _FromDictHelper(_cls, _d: dict, **overrides):
    _d = copy.copy(_d)  # Make it safe to remove elements.
    new_values = {}
    for f in fields(_cls):
        key = f.name
        if key not in _d: continue
        value = _d[key]
        del _d[key]
        if key in overrides:
            new_values[key] = overrides[key](value)
        else:
            new_values[key] = value
    assert len(_d) == 0
    return _cls(**new_values)


def _JsonDumpHelper(file, d: dict):
    json.dump(d, file, indent='\t', sort_keys=True)


@dataclass
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

    @classmethod
    def FromJson(cls, file) -> MKVFileTrack:
        return cls.FromDict(json.load(file))

    def ToDict(self) -> dict:
        return asdict(self)

    def ToJson(self, file) -> None:
        return _JsonDumpHelper(file, self.ToDict())


@dataclass
class MKVFile:
    file_path: str
    tracks: list[MKVFileTrack] = field(default_factory=lambda: [])

    @classmethod
    def FromDict(cls, d: dict) -> MKVFile:
        return _FromDictHelper(
                cls,
                d,
                tracks = lambda x: [MKVFileTrack.FromDict(t) for t in x])

    @classmethod
    def FromJson(cls, file) -> MKVFile:
        return cls.FromDict(json.load(file))

    def ToDict(self) -> dict:
        return asdict(self)

    def ToJson(self, file) -> None:
        return _JsonDumpHelper(file, self.ToDict())

@dataclass
class MKVDirectory:
    dir_path: str
    files: list[MKVFile] = field(default_factory=lambda: [])

    @classmethod
    def FromDict(cls, d: dict) -> MKVDirectory:
        return _FromDictHelper(
                cls,
                d,
                files=lambda files: [MKVFile.FromDict(file) for file in files])

    @classmethod
    def FromJson(cls, file) -> MKVDirectory:
        return cls.FromDict(json.load(file))

    def ToDict(self) -> dict:
        return asdict(self)

    def ToJson(self, file) -> None:
        return _JsonDumpHelper(file, self.ToDict())


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

    import os
    import tempfile
    with tempfile.TemporaryDirectory() as temp_dir:
        json_path = os.path.join(temp_dir, 'json')
        with open(json_path, 'w') as json_file:
            directory.ToJson(json_file)
        with open(json_path, 'r') as json_file:
            print(json_file.read())
        with open(json_path, 'r') as json_file:
            print(MKVDirectory.FromJson(json_file))
