#!/usr/bin/env python

import hashlib

def create_checksum(path):
    checksum = hashlib.md5()
    with open(path, "rb") as fp:
        while True:
            buffer = fp.read(8192)
            if not buffer: break
        checksum.update(buffer)
    checksum = checksum.hexdigest()
    return checksum

def main():
    file_path = 'test1.txt'
    md5_checksum = create_checksum(file_path)
    print(f'MD5 Checksum of {file_path}: {md5_checksum}')