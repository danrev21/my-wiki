#!/usr/bin/env python

# Keyword Arguments

def create_person_info(name, age, city):
    """
    Create a person's information string.
    :param name: The person's name.
    :param age: The person's age.
    :param city: The person's city.
    :return: A string containing the person's information.
    """
    info = f"Name: {name}, Age: {age}, City: {city}"
    return info

person_info = create_person_info(30, "Alice", "New York")
# or person_info = create_person_info(age=30, name="Alice", city="New York")
print(person_info)    # output: Name: 30, Age: Alice, City: New York