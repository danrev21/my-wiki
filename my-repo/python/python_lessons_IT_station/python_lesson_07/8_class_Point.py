#!/usr/bin/env python

# In this example, the Point class overloads the addition (+), 
# equality (==), and string representation (__str__) operators.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Special Methods: Methods in a class that begin and end with double underscores (dunder methods).
    # Overloading Operators: Providing a custom implementation for standard Python operators.
    # Commonly Overloaded Operators: __add__, __sub__, __eq__, __lt__, __str__, etc.
        
    # Overloading the addition operator 
    def __add__(self, other_point):
        return Point(self.x + other_point.x, self.y + other_point.y)

    # Overloading the equality operator
    def __eq__(self, other_point):
        return self.x == other_point.x and self.y == other_point.y

    # Overloading the string representation
    def __str__(self):
        return f"Point({self.x}, {self.y})"

# Creating instances of the Point class
point1 = Point(1, 2)
point2 = Point(3, 4)

# Using overloaded operators
sum_point = point1 + point2
are_equal = point1 == point2

print(f"Sum of points: {sum_point}")
print(f"Are points equal? {are_equal}")