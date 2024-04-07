#!/bin/bash

set -ueo pipefail

for dir in *; do
	if [ -d "$dir" ]; then
		cd "$dir"
		if [ -f "Makefile" ]; then
			echo ' == Creating "$dir" =='
			make clean
			make
			make view
		fi
		cd ..
	fi
done
