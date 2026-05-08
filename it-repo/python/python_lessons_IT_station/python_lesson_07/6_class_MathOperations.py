#!/usr/bin/env python

# In this example, add and subtract are static methods of the 
# MathOperations class. They don't require an instance of the class 
# to be created and can be called directly on the class itself.

class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

# Using static methods without creating an instance
result_addition = MathOperations.add(5, 3)
result_subtraction = MathOperations.subtract(8, 2)

print(f"Addition result: {result_addition}")
print(f"Subtraction result: {result_subtraction}")