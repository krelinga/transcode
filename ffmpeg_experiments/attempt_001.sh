#! /usr/bin/bash

readonly ffmpeg="/usr/bin/ffmpeg"

readonly input_file="/mnt/share/Ghost in the Shell Stand Alone Complex (2002)/Episode S01E01.mkv"
readonly output_file="/mnt/share/ffmpeg_out/Episode S01E01.mkv"

mkdir $(dirname "${output_file}") || exit 1
cp "${input_file}" "${output_file}"
