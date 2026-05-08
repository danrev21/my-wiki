#!/usr/bin/env python

# Arbitrary Arguments, *args
# output sum of values

def add(*values):
    sum = 0
    for i in values:
        sum += i
    return sum

print(add(1, 5, 2))  # output: 8