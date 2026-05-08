#!/bin/bash

# Script that checks the size of a given file.
# The script should take a single argument: the path to a file. 
# If the file's size is less than or equal to 1024 bytes, the script should display OK. 
# If the file's size exceeds 1024 bytes, the script should print FAIL.

[[ $(find . -name "$1" -size -1025c) ]] && echo "OK" || echo "FAIL"

# or using IF conditional:
#if [[ $(find . -name "$1" -size -1025c) ]]; then
#  echo "OK"
#else
#  echo "FAIL"
#fi

# To create test file: fallocate -l 1024 tinyfile.txt
# Base command: find . -name "tinyfile.txt" -size -1025c

