'''Data Classes for objects known to this system.'''


from dataclasses import dataclass, field


@dataclass(frozen=True)
class MKVFileTrack:
    track_id: int
    audio_channels: int = field(default=None)
    default_track: bool = field(default=None)
    forced_track: bool = field(default=None)
    language: str = field(default=None)
    track_name: str = field(default=None)
    track_type: str = field(default=None)


@dataclass(frozen=True)
class MKVFile:
    file_path: str
    tracks: list[MKVFileTrack] = field(default_factory=lambda: [])


@dataclass(frozen=True)
class MKVDirectory:
    dir_path: str
    files: list[MKVFile] = field(default_factory=lambda: [])


if __name__ == '__main__':
    track = MKVFileTrack(track_id=0, audio_channels=1, language='english')
    file = MKVFile(file_path='/foo/bar', tracks=[track])
    print(MKVDirectory(dir_path='/foo', files=[file]))
    print(file)
    print(track)
