#!/usr/bin/env python

# In this example, the get_length method is a getter method 
# that allows controlled access to the _length attribute, 
# and the set_length method is a setter method that ensures 
# the new length is valid.

# Encapsulation: Controlling access to the internal state of an object to prevent unintended interference.

class Rectangle:
    def __init__(self, length, width):
        self._length = length  # Convention: Use a single underscore "_" to indicate a "protected" attribute
        self._width = width

    def get_length(self):  # Getter Methods: used to retrieve the values of private or protected attributes.
        return self._length  

    def set_length(self, new_length): # Setter Methods: used to modify the values of private or protected attributes.
        if new_length > 0:
            self._length = new_length
        else:
            print("Length must be greater than 0.")

    def area(self):
        return self._length * self._width

# Creating an instance of the Rectangle class
rectangle = Rectangle(5, 3)

# Accessing attributes through methods
print(f"Initial Length: {rectangle.get_length()}")
rectangle.set_length(8)
print(f"Updated Length: {rectangle.get_length()}")
print(f"Area: {rectangle.area()}")