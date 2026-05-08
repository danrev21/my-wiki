#!/usr/bin/env python

# Write a script that backs up files from one directory into another, 
# preserving the directory structure and file metadata.

# Requirements:
# Recursively copy all files and directories from the source to the destination.
# Preserve file metadata.
# Ensure the directory structure is maintained in the backup location.
# Example:
# A file src/documents/report.txt should be backed up to backup/documents/report.txt.

# Tips:
# Use the shutil module for copying files and directories.
# Use shutil.copy2 to preserve metadata.
# Make sure to handle any exceptions that may occur.

import shutil
import errno

# function to copy the entire directory 
# tree from src to dest:
def copy_backup(src = ".", dest = "./backup/documents/"):

    # the errno module is used to check the type of error, 
    # and if the error is due to the source 
    # not being a directory (errno.ENOTDIR), then shutil.copy2() 
    # is used to copy the source file to the destination.
    try:
        shutil.copytree(src, dest)
    except OSError as err:
 
        # error caused if the source was not a directory
        if err.errno == errno.ENOTDIR:
            shutil.copy2(src, dest)
        else:
            print("Error: {}".format(err))

if __name__ == "__main__":
    
    copy_backup()  # define Source path and Destination path:    