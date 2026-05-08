#!/bin/bash

if [ ! -f data.txt ]
then
    echo "File does not exist in Bash"
else
    echo "File data.txt found!"
    cp data.txt backup.txt 2> /dev/null
fi
