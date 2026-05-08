#!/usr/bin/env python

person = {'name': 'John', 'age': 30, 'city': 'New York'}

keys = person.keys()
values = person.values()
items = person.items()

print(keys)    # Output: dict_keys(['name', 'age', 'city'])
print(values)  # Output: dict_values(['John', 30, 'New York'])
print(items)   # Output: dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])

# Adding a new key-value pair
person['occupation'] = 'Engineer'   # Output: {'name': 'John', 'city': 'New York', 'occupation': 'Engineer'}
print(person)         # Output: {'name': 'John', 'city': 'New York', 'occupation': 'Engineer'}

# Removing a key-value pair
removed_item = person.pop('age')    
print(removed_item)   # Output: 30