#! /usr/bin/bash

readonly ffmpeg="/usr/bin/ffmpeg"

readonly input_file="/mnt/share/Ghost in the Shell Stand Alone Complex (2002)/Episode S01E01.mkv"
readonly output_file="/mnt/share/ffmpeg_out/Episode S01E01.mkv"
readonly log_file_output="$(dirname "$0")/attempt001.log"

mkdir -p $(dirname "${output_file}") || exit 1
# This invocation was taken from https://stackoverflow.com/questions/5678695/ffmpeg-usage-to-encode-a-video-to-h264-codec-format .
# Info about redirecting ffmpeg logs from: https://stackoverflow.com/questions/2066076/how-do-i-enable-ffmpeg-logging-and-where-can-i-find-the-ffmpeg-log-file
# Note that right now this method of log storage is somewhat unsatisfying, because all of the terminal progress outputs are also written to the log.
export FFREPORT="file=${log_file_output}:level=32"  # 32 is an alias for INFO
"${ffmpeg}" -i "${input_file}" -vcodec libx264 -acodec aac "${output_file}"
