#!/usr/bin/env python

# здесь создаваемые объекты будут иметь уже три атрибута: разные 
# для каждого объекта name и age, и одинаковый для всех объектов - university
class Student:
    # Class attribute
    university = "XYZ University"

    def __init__(self, name, age):
        # creating attributes
        self.name = name
        self.age = age

    # Creating and Using Class Method
    def display_info(self):
        print(f"{self.name} is {self.age} years old.")

# Creating instances (objects) of the Student class
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

# Accessing class attribute
print(f"{student1.name} attends {Student.university}")

# Calling instance method
student2.display_info()

# output:
# Alice attends XYZ University
# Bob is 22 years old.

# Importing class:
# from class_Student import Student
# stud1 = Student("Dan", 21)
# print(stud1.name)
# print(stud1.university)
# stud1.display_info()
# Output:
# Dan
# 21
# XYZ University
# Dan is 21 years old.



