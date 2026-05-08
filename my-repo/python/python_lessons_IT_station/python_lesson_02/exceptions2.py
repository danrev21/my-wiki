#!/usr/bin/env python

# here we get "LOL" instead of: 
# TypeError: unsupported operand 
# type(s) for +: 'set' and 'set'

try:
    a = {1,2,3}
    b = {3,4,5}
    print(a + b)
except TypeError: print("LOL")   