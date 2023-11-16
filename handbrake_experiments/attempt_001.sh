#! /usr/bin/bash

readonly handbrake="/usr/bin/HandBrakeCLI"

readonly input_file="/mnt/share/Ghost in the Shell Stand Alone Complex (2002)/Episode S01E01.mkv"
readonly output_file="/mnt/share/handbrake_out/Episode S01E01.mkv"

"${handbrake}" -i "${input_file}" -o "${output_file}"
