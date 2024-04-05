#!/bin/bash

set -ueo pipefail

for dir in *; do
	if [ "$dir" == "dso" ]; then
		echo "Skipped"
	elif [ -d "$dir" ]; then
		cd "$dir"
		cd "res"
		lualatex $(ls *.tex)
		cd ..
		lualatex "$dir".tex
		lualatex "$dir".tex
		lualatex "$dir".tex
		cd ..
	fi
done