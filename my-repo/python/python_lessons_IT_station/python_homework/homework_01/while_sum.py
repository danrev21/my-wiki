#!/usr/bin/env python

# program that asks the user to input 
# numbers until they enter a negative number. 
# Calculate and print the sum of all the 
# positive numbers entered.

total = 0
while True:
    num = int(input("Enter a number (negative number to stop): "))
    if num < 0:
        break
    total += num
print("Sum:", total)