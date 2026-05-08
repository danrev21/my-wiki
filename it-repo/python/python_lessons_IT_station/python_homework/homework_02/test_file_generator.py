#!/usr/bin/env python

# Create a script that writes a line to a file a specified number of times.
# Requirements:
# Scripts read following input args:
#               file name
#               phrase
#               number of repetion phrase
# Script name: test_file_generator.py

# script writes lines in file
with open('file.txt', 'a') as file:
    l1 = "Welcome to TutorialsPoint\n"
    l2 = "Write multiple lines \n"
    l3 = "Done successfully\n"
    l4 = "Thank You!"
    file.writelines([l1, l2, l3, l4])
file.close()