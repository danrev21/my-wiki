#!/usr/bin/env python

# Default Parameter Value

def greet(name="Stranger"):
    """
    Greet a person with an optional name.
    :param name: The name of the person to greet (default is "Stranger").
    """
    print(f"Hello, {name}!")

# Calling the function without an argument, using the default value
greet()        # output: Hello Stranger!

# Calling the function with an argument
greet("Alice")  # output: Hello Alice!