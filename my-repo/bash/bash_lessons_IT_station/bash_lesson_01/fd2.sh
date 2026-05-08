#!/usr/bin/env bash

echo "This is a standard output that will be silenced" > /dev/null
echo "This is an error message that will be silenced" >&2 > /dev/null
