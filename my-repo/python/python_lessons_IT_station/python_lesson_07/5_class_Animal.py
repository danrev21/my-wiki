#!/usr/bin/env python

# Inheritance is a fundamental concept in OOP that allows a new class (subclass) 
# to inherit attributes and methods from an existing class (parent or superclass).
# The subclass can then extend or override inherited functionality.

# In this example, the Dog and Cat classes are subclasses of the Animal class. 
# They inherit the species attribute and the make_sound method from the superclass.

class Animal:  # общий класс, из которого будут наследоваться атрибуты в subclasses
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        pass  # Placeholder for the sound each animal makes

# Subclass (Dog) inherits from the superclass (Animal)
class Dog(Animal):
    def __init__(self, breed):
        # Calling the constructor of the superclass
        super().__init__("Dog") 
        self.breed = breed

    # Method Overriding: Providing a specific implementation of 
    # a method in the subclass that is already defined in the superclass.
    def make_sound(self):
        return "Woof!"

# Subclass (Cat) also inherits from the superclass (Animal)
class Cat(Animal):
    def __init__(self, breed):
        super().__init__("Cat")
        self.breed = breed

    # Overriding the make_sound method
    def make_sound(self):
        return "Meow!"

# Creating instances of the subclasses
dog = Dog("Labrador")
cat = Cat("Siamese")

# Accessing attributes and calling methods
print(f"{dog.species} of breed {dog.breed} says: {dog.make_sound()}")
print(f"{cat.species} of breed {cat.breed} says: {cat.make_sound()}")