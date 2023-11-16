## Handbrake experiments

I'm going to try playing around with more handbrake options for encoding ... I suspect this may just "do the right thing" in cases like anamorphic widescreen without me having to feed it so much guidance.

### attempt_001.sh

This produces working output, with a few issues:

- only one audio track is included.
- no subtitle tracks are included.
- the output video looks interlaced ... not sure if this is really all that much of a problem but worth calling out.

### attempt_002.sh

This produces working output, but it has no audio at all and no subtitles.  Also the video quality is overall low, and the file size is tiny (only 80 MiB).

### attempt_003.sh

This produces working output, with all audio tracks.  It seems to only include one subtitle track, and it seems to get burned into the video....
