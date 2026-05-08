#!/usr/bin/env python

# Create a script that organizes files in a directory into subdirectories based on file type.
# Requirements:
# Scan a specified directory.
# Create a new directory for each unique file extension.
# Move each file into the corresponding directory based on its file extension.

import os
import shutil

# generating files with extensions 'txt', 'scv', 'png'
def create_files_ext(path = "/tmp/my_dir"):           
    if not os.path.exists(path):
        os.mkdir(path)
    def file_recursion(i):
        with open(os.path.join(path, "file_test0" + str(i) + ".txt"), "a") as file:
            file.write("It is simple 'TXT' file")      
            file.close()
        with open(os.path.join(path, "file_test0" + str(i) + ".scv"), "a") as file:
            file.write("It is 'SCV' file") 
            file.close()
        with open(os.path.join(path, "file_test0" + str(i) + ".png"), "a") as file:
            file.write("This string will increase the size of 'png' files") 
            file.close()
        if i == 0:
            return 1
        else:
            file_recursion(i-1)
    file_recursion(9)
create_files_ext()

# organize the files   
def files_organiser(path = "/tmp/my_dir"):    # file location path
    if not os.path.exists(path):
        os.mkdir(path)
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:            
            original_file_path = os.path.join(path, f)           # Path to the original file           
            if os.path.isfile(original_file_path):               # Only operate on files               
                file_name = os.path.basename(original_file_path) # Get file name portion only                
                extension = f.split(".")[-1]                     # Get the extension of the file and create a path for it
                extension_path = os.path.join(path, extension)                
                if not os.path.exists(extension_path):           # Create the path for files with the extension if it doesn't exist
                    os.makedirs(extension_path)                
                shutil.move(original_file_path, os.path.join(extension_path, file_name)) # for safe using 'copy' is better

if __name__ == "__main__":   
    files_organiser()           # specify the location of your files