#!/usr/bin/env python

# program that asks the user to input two numbers and performs division. 
# Handle the ZeroDivisionError and ValueError exceptions gracefully, 
# providing informative error messages.

while True:
    try:
        num1 = int(input("Input num1: "))
        num2 = int(input("Input num2: "))
        print(f"Division result is: {num1/num2}")
        break
    except ValueError:
        print("Wrong input. Try again.")
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
        