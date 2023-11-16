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

### attempt_004.sh

OK, at this point all of the audio & subtitle tracks are included (and not burned in), and the aspect ratio is correct.

The next step is to try to increase the overall video quality, and possibly tackle the interlacing issue.

### attempt_005.sh

I tried setting quality = 16 in this run, and there wasn't a huge difference between this and the default quality = 22 run.  I think the next thing that I'll try is running with one of the h264 presets and seeing if that helps anything.

### attempt_006.sh

This attempt tries to use one of handbrake's presets, which seems to work pretty well.  In fact the audio compression here shrinks the file vs. my old set of options, for similar video quality.  Also confirmed that all of the audio & subtitle tracks are present (and not burned in).  The video also appears to be deinterlaced.

I think the next thing to try is probably to tweak settings around default audio tracks (and see if that even matters from Jellyfin's point of view).  Also (of course) try uploading this to Jellyfin and see what it thinks of the encoding.  How much CPU will it spend on re-encoding the container format?
