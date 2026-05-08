#!/usr/bin/env python

# Develop a script that reports the disk usage of each subdirectory within a given directory.

# Requirements:
# Traverse the specified directory and all subdirectories.
# Calculate the total size for each subdirectory.
# Identify and list the largest files.
# Output:
# Print a report of the total size of each subdirectory and the top 5 largest files in the entire directory tree.

# Tips:
# Use the os module to traverse directories.
# Calculate sizes using os.path.getsize.
# Consider using a priority queue or sorting for managing the largest files.

import os

# Calculating the total size for specified directory
def dir_size(path):
    total_size = 0
    for dirnames, subdirnames, filenames in os.walk(path):     # traversing the specified directory
        for file in filenames:
            file_path = os.path.join(dirnames, file)
            if not os.path.islink(file_path):
                total_size += os.path.getsize(file_path)
    for unit in ['B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB']:      # making size output is readable
        if total_size < 1024.0 or unit == 'PiB':
            break
        total_size /= 1024.0
    print(f"Size of '{path}':  {round(total_size, 2)} {unit}")

# Calculating the total size for each subdirectory using previous function
def subdir_size(path):
    for dirnames, subdirnames, filenames in os.walk(path):      # traversing subdirectories
        for dir in subdirnames:
            subdir_path = os.path.join(dirnames, dir)
            dir_size(subdir_path)
  

# using a priority queue and sorting for managing the largest files
from queue import PriorityQueue                                # PriorityQueue class is part of the queue module

def largest_files(num_largest_files, path):

    q = PriorityQueue()                                         # creating priority queue

    for dirnames, subdirnames, filenames in os.walk(path):      # traversing the specified directory
        for file in filenames:
            file_path = os.path.join(dirnames, file)
            if not os.path.islink(file_path):
                file_size = os.path.getsize(file_path)
                q.put((file_size, file_path))                   # adding in queue sizes and paths of all files in specified dir
    collect = []                                                # define the empty list named 'collect'
    while not q.empty():                                        # append elements of queue in list
        item = q.get()
        collect.append(item)
        collect.sort(reverse=True)                              # т.к. элементы из queue выгружаются в порядке возрастания, делаем реверс 'collect' 
        c = collect[0:num_largest_files]
    print("----------------------\nThe largest files are:")
    for max_size in c:
        print(max_size)


if __name__ == "__main__":

    path = '/tmp/my_dir/'      # specify your directory path

    dir_size(path)
 
    subdir_size(path)

    largest_files(5, path)