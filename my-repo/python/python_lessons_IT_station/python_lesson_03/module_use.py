#!/usr/bin/env python

# Code Example - Importing a Custom Python File:

# Assuming you have a custom Python file 
# named my_module.py with the following content:

# module_use.py:

def greet(name):
    return f"Hello, {name}!"

def square(x):
    return x * x

"""
# You can import and use functions from this 
# custom file in another Python script as follows:

# main_script.py:

import module_use  # Import the custom Python file

# Use functions from the custom module
message = module_use.greet("Alice")
print(message)                          # output: Hello, Alice!

result = module_use.square(5)
print(f"The square of 5 is {result}")   # output: The square of 5 is 25

# In this example my_module.py defines two functions, greet() and square().
# main_script.py imports the my_module custom Python file using the import statement.
# The functions from my_module are then called and used in the main_script.py.
# This demonstrates how you can import functions from your custom Python files 
# to reuse code and keep your code organized.
"""
