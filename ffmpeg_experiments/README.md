## ffmpeg experiments

The goal here is to be able to transcode directly with ffmpeg and not use handbrake.

This is interesting because I want to have more control over how the transcoding works, including things like my own logic to select subtitle tracks, output formats, etc.  Also, this is just a chance to learn stuff!

### chapter_split.sh

This is my attempt to split up the MKV file that I was using for testing at chapter boundaries.  The idea was to make it easier to experiment with by using a smaller file, which should improve ffmpeg runtimes.

In the current incarnation, the aspect ratio is not respected for some reason ... the output chapter splits seem to be 4:3 in a way that just truncates the wider parts of the image.

### attempt_001.sh

This command does invoke ffmpeg, but it has several problems:
- Only one audio track is preserved.
- no subtitle tracks are preserved.
- the video aspect ratio is wrong ... the output video is horizontally-compressed.

### attempt_002.sh

This is better in that it seems to preserve all of the subtitles & audio tracks, but still has some problems:
- the "default" bit in the audio track metadata is only retained in the case where it is set to "false".
- the aspect ratio is still messed up.

### attempt_003.sh

This attempt introduces the `-aspect` flag, which didn't seem to help at all.
