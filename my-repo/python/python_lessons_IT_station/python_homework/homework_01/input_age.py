#!/usr/bin/env python

# program that takes a user's input for 
# their age and tells them if they are:
#    child  ...12
#    teenager  13...18 
#    adult     19... 

age = float(input("Please, input your age: "))
if 0 < age < 13:
    print("You are a child.")
elif 13 <= age <= 18:
    print("You are a teenager!")
elif age > 18:
    print("You are an adult.")
else:
    print("You're about to be born!")
