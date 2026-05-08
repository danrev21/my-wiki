#!/usr/bin/env python

# In this example, Shape is an abstract class with two abstract methods, 
# area and perimeter. The Rectangle class is a concrete subclass of Shape 
# that provides implementations for these abstract methods.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Attempting to create an instance of an abstract class will result in an error
# shape = Shape()  # Uncommenting this line will raise an error

# Subclass (Rectangle) providing concrete implementations for abstract methods
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Creating an instance of the subclass
rectangle = Rectangle(4, 3)

# Accessing methods of the subclass
print(f"Area: {rectangle.area()}")
print(f"Perimeter: {rectangle.perimeter()}")