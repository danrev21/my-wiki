#!/usr/bin/env python

# print all odd numbers from 1 to 50, 
# skipping even numbers.

for i in range(1, 50):
    if i % 2 == 0:
        continue
    print(i)