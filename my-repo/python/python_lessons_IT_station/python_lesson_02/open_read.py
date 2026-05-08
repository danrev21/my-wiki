#!/usr/bin/env python

# Reading from a file
with open("file.txt", "r") as file:
    content = file.read()
    print(content)

### if needed to save object open("file.txt", "r"):
# file = open("file.txt", "r")
# print(file.read())