#! /usr/bin/bash

readonly mkv_merge="/usr/bin/mkvmerge"
readonly input_file="/mnt/share/Ghost in the Shell Stand Alone Complex (2002)/Episode S01E01.mkv"
readonly output_file="/mnt/share/chapter_split_out/s01e01.mkv"

"${mkv_merge}" -o "${output_file}" --split chapters:all "${input_file}"

