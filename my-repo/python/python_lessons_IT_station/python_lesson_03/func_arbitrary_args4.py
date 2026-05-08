#!/usr/bin/env python

# Arbitrary Arguments, *args
# first - required parameter

def concatenate_strings(first, *args):
 
    result = first
    for s in args:
        result += s
    return result

combined = concatenate_strings("Hello, ", "great ", "world", "!")
print(combined)     # output: Hello, world!