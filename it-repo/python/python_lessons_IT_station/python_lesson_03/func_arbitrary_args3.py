#!/usr/bin/env python

# Arbitrary Arguments, *args

def concatenate_strings(*args):
    """
    Concatenate a list of strings.
    :param args: Strings to concatenate.
    :return: The concatenated string.
    """
    result = ""
    for s in args:
        result += s
    return result

combined = concatenate_strings("Hello, ", "world", "!")
print(combined)     # output: Hello, world!