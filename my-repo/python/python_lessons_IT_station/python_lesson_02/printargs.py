#!/usr/bin/env python

import sys

if len(sys.argv) > 1:
    script_name = sys.argv[0]
    argument = sys.argv[1:]    # output all arguments
    print(f"Script name: {script_name}")
    print(f"Command-line argument: {argument}")
else:
    print("No command-line arguments provided.")
