#!/usr/bin/env python

# Arbitrary Arguments, *args
# output sum of lists values:

def add(*values):
    sum = 0
    for i in values:
        for j in i:
            sum += j
    return sum

print(add([1,2,3],[1,2,3])) # output: 12