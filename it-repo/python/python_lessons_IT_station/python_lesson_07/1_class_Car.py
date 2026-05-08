#!/usr/bin/env python

# создаваемые объекты будут иметь два атрибута (метода)- make и model
class Car:
    def __init__(self, make, model):  # constructor
        self.make = make              # Class attributes are variables that store data shared among all instances of a class.
        self.model = model

# Creating instances (objects) of the Car class
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

# Accessing attributes
print(f"Car 1: {car1.make} {car1.model}")
print(f"Car 2: {car2.make} {car2.model}")

print(car1.make)  # объект car1 с атрибутом make
print(car1.model) # объект car1 с атрибутом model

# output:
# Car 1: Toyota Camry
# Car 2: Honda Civic
# Toyota
# Camry

# можно импортировать:
# from class_Car import Car
# bmw = Car("BMW", 3)
# audi = Car("AUDI", "A3")
# print(bmw.make)
# print(bmw.model)
# output:
# BMW
# 3

