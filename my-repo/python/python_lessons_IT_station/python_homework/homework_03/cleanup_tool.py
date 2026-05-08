#!/usr/bin/env python

# Develop a script that cleans up a directory by removing empty subdirectories 
# and files older than a certain date.

# Requirements:
# Identify and remove all empty subdirectories within a given directory.
# Identify and remove files that were last modified before a specified date.
# Implement error handling to manage exceptions like PermissionError.
# Example:
# If the script is set to remove files older than 2023-01-01, then a file with 
# a last modified date of 2022-12-25 should be removed.

# Tips:
# Use os.walk for directory traversal.
# Use os.path.getmtime to check the last modified time of files.
# Implement try-except blocks to handle possible exceptions.

import os
import shutil
import time

# preparing directories for script
shutil.rmtree("./clean_work")
shutil.copytree("./clean_template", "./clean_work")

# function converting Unix time to readable time
def time_from_unix(unix_timestamp):
    time_struct = time.localtime(unix_timestamp)
    utc_time = time.strftime("%Y-%m-%d %H:%M:%S", time_struct)
    return utc_time

# Identify and remove all empty subdirectories within a given directory
def remove_empty_dirs(path):
    for dirnames, subdirnames, filenames in os.walk(path):
        for dirs in subdirnames:
            del_path = os.path.join(dirnames, dirs)
            try:
                os.rmdir(del_path)
                print(f"Empty directory {del_path} removed.")
            except OSError:
                print(f"The directory {del_path} is not empty")

# function listing files with modify time
def list_mtime_files(path):         
    for dirnames, subdirnames, filenames in os.walk(path):
        for files in filenames:
            files_path = os.path.join(dirnames, files)
            unix_mtime = os.path.getmtime(files_path)       # getting modify time file in UNIX format
            utc_mtime = time_from_unix(unix_mtime)          # converting from UNIX to UTC time
            print(f"Last modification time {files_path}: {utc_mtime}")         

# Identify and remove files that were last modified before a specified date.
# def remove_modified_files(specified_time):            
def remove_modified_files(path):
    for dirnames, subdirnames, filenames in os.walk(path):
        for files in filenames:
            files_path = os.path.join(dirnames, files)
            unix_mtime = os.path.getmtime(files_path)       # getting modify time file in UNIX format
            utc_mtime = time_from_unix(unix_mtime)          # converting from UNIX to UTC time
            if unix_mtime < specified_unix_time:
                try:
                    print(f"File: {files_path} {utc_mtime} removed!")
                    os.remove(files_path)
                except PermissionError:
                    print("Removing not permitted")

if __name__ == "__main__":

    path = "./clean_work"

    remove_empty_dirs(path)
    list_mtime_files(path)
    specified_time = input('\nPlease, specify the modification time of the file.\nAll files modified earlier this file will be deleted (input format - "2023-12-24 22:19:00"): ')
    specified_unix_time = float(time.mktime(time.strptime(specified_time, '%Y-%m-%d %H:%M:%S')))
    remove_modified_files(path)