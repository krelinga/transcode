#! /usr/bin/bash

readonly handbrake="/usr/bin/HandBrakeCLI"

readonly input_file="/mnt/share/Ghost in the Shell Stand Alone Complex (2002)/Episode S01E01.mkv"
readonly output_file="/mnt/share/handbrake_out/Episode S01E01.mkv"
readonly log_file_output="$(dirname "$0")/attempt_002.log"

"${handbrake}" -i "${input_file}" -o "${output_file}" 2> "${log_file_output}" \
    -e x264 \
    --audio-lang-list und \
    --all-audio \
    -E copy \
    --non-anamorphic \
    --subtitle-lang-list und \
    --all-subtitles \
    --subtitle-burned none
