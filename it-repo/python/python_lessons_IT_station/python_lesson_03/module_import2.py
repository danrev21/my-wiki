#!/usr/bin/env python

"""
This small program first imports the random module 
on the first line, then moves into a for loop 
which will be working with 10 elements. Within the loop, 
the program will print a random integer within the 
range of 1 through 25 (inclusive). 
The integers 1 and 25 are passed to random.randint() 
as its parameters.
"""
import random


for i in range(10):
    print(random.randint(1, 25))

# Output
# 6
# 9
# 1
# 14
# 3
# 22
# 10
# 1
# 15
# 9