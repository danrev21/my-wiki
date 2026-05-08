#!/usr/bin/env python

"""
Decorators
In Python, decorators are a powerful way to modify or enhance the behavior of 
functions or methods without changing their source code. Decorators are often 
used for tasks like logging, authentication, and access control. 
Here are some key points to consider:
  Decorator Function: A decorator is a function that takes another function as 
an argument and returns a new function that usually extends or modifies the 
behavior of the original function.
  Syntax: Decorators are typically applied using the @decorator_function 
syntax just above the function definition.
  Common Use Cases: Decorators can be used for tasks like adding logging, 
authentication checks, caching, and more to existing functions.

Code Example - Creating a Simple Decorator:
"""

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.

"""
In this example:
The my_decorator function takes another function, func, and returns 
a new function, wrapper, that adds behavior before and after the original function.
The @my_decorator decorator is applied to the say_hello function, enhancing its behavior.
When say_hello() is called, it includes the behavior added by the decorator.
Decorators provide a clean and reusable way to modify the behavior of functions or 
methods, making them a valuable tool in Python for aspects like code organization and 
adding additional functionality to existing code.
"""