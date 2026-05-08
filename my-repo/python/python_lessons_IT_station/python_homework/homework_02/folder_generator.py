#!/usr/bin/env python

# Requirements:
# create a target folder if not exists
# function which create 10 folders inside(10 is default value, 
# funcsion should have input argument with folders quantity)
# main part which create 10 folders and then 10 folders inside each one.

import os 
import sys
import glob

# creating a target directory in '/tmp' if not exists
def parent(i):  
    path = "."
    items = 0
    for items in range(i):
        folder = path + "/test0" + str(items)
        if not os.path.exists(folder):
            os.makedirs(folder)
            items += 1

# creating inside directories (10 is default value, function have input argument with directories quantity)
def inside(*num):
    path = "."
    for folder in glob.iglob(path + "/test0*"):
        items = 0
        for items in range(*num):
            path = os.path.join(folder, "test0" + str(items)) 
            os.mkdir(path)
            items += 1          

# main part which create 10 directories and then 10 directories inside each one or specified number of directories 
if __name__ == "__main__":
    parent(10)
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
        inside(num)
    else:
        inside(10)