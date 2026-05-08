#!/bin/bash

[ -f "data.txt" ] && echo "File data.txt found!"
cp data.txt backup.txt 2> /dev/null
[ -f "data.txt" ] || echo "File data.txt not found!"
