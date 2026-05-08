#!/usr/bin/env python

# Write function that creates 10 files with target content inside target folder.
# Requirements:
# function name: createTenFilesInDir(path, phrase="default_text")
# input args: path to target dir, content for each file
# tip: try to use recursion for it

import os

def createTenFilesInDir(path, phrase="default_text"):

    def file_recursion(i):              # creating file with content using recursion function
        file_path = os.path.join(path, "file_test0" + str(i))
        with open(file_path, "a") as file:
                file.writelines(f"{phrase}\n")  # adding phrase lines into file
                file.close()
        if i == 0:
            return 1
        else:
             file_recursion(i-1)

    file_recursion(9)
    
if __name__ == "__main__":
    createTenFilesInDir("/tmp", "default_text")