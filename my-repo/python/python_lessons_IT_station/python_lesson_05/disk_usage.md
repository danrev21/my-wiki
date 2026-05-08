#!/usr/bin/env python

import os
import shutil

-------------------------------------------------------------------------
disk_usage = shutil.disk_usage('/')
print(f"Total: {disk_usage.total} bytes")
print(f"Used: {disk_usage.used} bytes")
print(f"Free: {disk_usage.free} bytes")

-------------------------------------------------------------------------
# human readable size
def human_readable_size(size, decimal_places=2):
    for unit in ['B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB']:
        if size < 1024.0 or unit == 'PiB':
            break
        size /= 1024.0
    return f"{size:.{decimal_places}f} {unit}"

-------------------------------------------------------------------------
# files size
def get_dir_size(dir_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            if not os.path.islink(file_path):
                files_size = os.path.getsize(file_path)
                total_size += os.path.getsize(file_path)
                print(file_path, files_size)
get_dir_size('/tmp')

-------------------------------------------------------------------------
# getting size of directories

# Using os.path.getsize() will only get you the size of the directory, NOT of its content. 
# So if you call getsize() on any directory you will always get the same size since they are 
# all represented the same way. On contrary, if you call it on a file, it will return the actual file size.
# If you want the content you will need to do it recursively, like below:

sum([os.path.getsize(f) for f in os.listdir('.') if os.path.isfile(f)])

-------------------------------------------------------------------------






