#!/usr/bin/env python

import os 
import re
import shutil
import glob

-------------------------------------------------------------------------
# creates folders as defined in list

import os 
root_path = '/home/dan/Workdir/it_station_lab/HW/python_lessons/python_lesson_05/homework/gen/'
list = ['car', 'truck', 'bike', 'cycle', 'train'] 
for items in list: 
    path = os.path.join(root_path, items) 
    os.mkdir(path) 

-------------------------------------------------------------------------
# create a target folder if not exists
# function which create folders inside
folder = "test00"
isExist = os.path.exists(folder)
if not isExist:
   os.makedirs(folder)
def inside():
    list = ['car', 'truck', 'bike', 'cycle', 'train'] 
    for items in list: 
        path = os.path.join(folder, items) 
        os.mkdir(path) 
inside()

-------------------------------------------------------------------------
# create one folder 'test00'and in it function creates defined number of folders 'test0x'
folder = "test00"
isExist = os.path.exists(folder)
if not isExist:
   os.makedirs(folder)

def inside(num):
    items = 0
    for items in range(num):
        path = os.path.join(folder, 'test0' + str(items))
        os.mkdir(path)
        items += 1
    return        
num = int(sys.argv[1])
inside(num)

-------------------------------------------------------------------------
# function create defined number of folders
def parent(i):
    items = 0
    for items in range(i):
        folder = "test0" + str(items)
        isExist = os.path.exists(folder)
        if not isExist:
            os.makedirs(folder)
            items += 1
parent(1)

-------------------------------------------------------------------------
# remove dirs   
pattern = r'test0*'
for f in os.listdir("."):
    if re.search(pattern, f):
        shutil.rmtree(f)

-------------------------------------------------------------------------        
# create list of dirs with names 'test0x'
current = os.getcwd()
list_dirs = os.listdir(current)
list_dirs.sort()
r = re.compile("test0*")
new_list = list(filter(r.match, list_dirs))
print(new_list)

-------------------------------------------------------------------------
# creating a target folderS if not exists
items = 0
for items in range(10):
    folder = "test0" + str(items)
    if not os.path.exists(folder):
        os.makedirs(folder)
        items += 1

-------------------------------------------------------------------------
# creating folders inside (10 is default value, function have input argument with folders quantity)
def inside(*num):
    for folder in glob.iglob("test0*"):
        items = 0
        for items in range(*num):
            path = os.path.join(folder, 'test0' + str(items)) 
            os.mkdir(path)
            items += 1          

-------------------------------------------------------------------------
# main part which create 10 folders and then 10 folders inside each one.
if __name__ == '__main__':
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
        inside(num)
    else:
        inside(10)

-------------------------------------------------------------------------
# iteration with for loop
directory = '/my_directory'
for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        #filename.startwith('file')
        with open(os.path.join(directory, filename)) as f:
            print(f.read()) 

-------------------------------------------------------------------------
# iteration with walk()
directory = '/my_directory'
for dirpath, dirnames, filenames in os.walk(directory):
    for filename in filenames:
        if filename.endswith('.txt'):
            with open(os.path.join(dirpath, filename)) as f:
                print(f.read())      

-------------------------------------------------------------------------
# iteration with for loop
a = 0
for a in range(10):
    i = 0
    for i in range(10):
        path2 = path + "/test0" + str(a) + "/test0" + str(i)
        os.chdir(path2) 
        file_generator.createTenFilesInDir(path2, "param pam pam")
        i += 1
    a += 1        

-------------------------------------------------------------------------
# iteration with for loop
a = 0
for a in range(10):
    
    i = 0
    for i in range(10):
        file_generator.createTenFilesInDir(path + "/test0" + str(a) + "/test0" + str(i), "param pam pam")
        i += 1
    a += 1       

-------------------------------------------------------------------------
# поиск файлов с расширением и перемещение
for dirpath, dirnames, filenames in os.walk(destination_path):
    for file in filenames:
        source_file = f"/tmp/my_dir/{file}"
        dest_file = f"/tmp/my_org_dir/{file}"
        if file.endswith('.txt'):
            shutil.move(source_file, dest_file)                          

















