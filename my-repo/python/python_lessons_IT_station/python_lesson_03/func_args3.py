#!/usr/bin/env python

# script creates file with defined phrase and number of repetions this phrase

def file_gen(filename, phrase, number):
    for i in range(0, number):
        with open(filename, 'a') as file:
            file.writelines(f"{phrase}\n")
        file.close()        
file_gen('test.txt', 'Hello!', 5)