#!/usr/bin/env python

# Script which used logic from previous exersise and generate 
# folder with 10 test folders which contains 10 folder inside each, 
# and each folder should have 10 files inside.

# Requirements:
# script name: test_folder_generator.py
# import logic from previous scripts

import os
import folder_generator
import file_generator

def files_in_folders(path_dir = "/tmp/test_dir", \
                     par_num = 10, \
                     ins_num = 10, \
                     phrase = "default_text"):

    if not os.path.exists(path_dir):             # creating target directory
        os.mkdir(path_dir)

    os.chdir(path_dir)    

    folder_generator.parent(par_num)                # parent 'test' directories creating
    print(f"10 parent directories in '{path_dir}' created!")
    
    folder_generator.inside(ins_num)                # inside 'test' directories creating
    print(f"10 inside directories created!")

    a = 0                                           # files creating with path iteration
    for a in range(10):
        i = 0
        for i in range(10):
            path_files = path_dir + "/test0" + str(a) + "/test0" + str(i)
            os.chdir(path_files) 
            file_generator.createTenFilesInDir(path_files, "DevOps Belarus")
            i += 1
        a += 1        
    print(f"10 files in each inside folder created!")

if __name__ == "__main__":
    files_in_folders()




           

        