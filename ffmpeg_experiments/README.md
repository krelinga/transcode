## ffmpeg experiments

The goal here is to be able to transcode directly with ffmpeg and not use handbrake.

This is interesting because I want to have more control over how the transcoding works, including things like my own logic to select subtitle tracks, output formats, etc.  Also, this is just a chance to learn stuff!

### attempt_001.sh

This command does invoke ffmpeg, but it has several problems:
- Only one audio track is preserved.
- no subtitle tracks are preserved.
- the video aspect ratio is wrong ... the output video is horizontally-compressed.
