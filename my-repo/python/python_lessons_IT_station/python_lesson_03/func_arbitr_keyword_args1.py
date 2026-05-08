#!/usr/bin/env python

# Arbitrary Keyword Arguments, **kwargs

def display_info(**kwargs):
    """
    Display information about a person.
    :param kwargs: Keyword arguments representing person's attributes.
    """
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=30, country="USA")
# output: name: Alice
#         age: 30
#         country: USA
