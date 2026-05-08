# ntroduction: JSON (JavaScript Object Notation) is a lightweight data interchange format. The json module in Python provides tools for encoding Python objects as JSON and decoding JSON into Python objects.

-----------------------------------------------------------------------------------
# Encoding Python Objects into JSON: To convert a Python object into its JSON representation, use the json.dumps() function.
# In this example, the Python dictionary data is encoded into a JSON-formatted string.

import json
# Python dictionary
data = {'name': 'John Doe', 'age': 30, 'city': 'New York'}
# Encoding Python dictionary to JSON
json_data = json.dumps(data)
# Printing the JSON data
print(json_data)

-------------------------------------------------------------------------------------
# Decoding JSON into Python Objects: Conversely, to convert a JSON string into a Python object, use the json.loads() function.
# Here, the JSON-formatted string is decoded into a Python dictionary.

import json
# JSON-formatted string
json_data = '{"name": "Jane Smith", "age": 25, "city": "San Francisco"}'
# Decoding JSON to Python dictionary
data = json.loads(json_data)
# Accessing data
print(f"Name: {data['name']}, Age: {data['age']}, City: {data['city']}")

------------------------------------------------------------------------------------
# Working with JSON Files: The json module also simplifies working with JSON files using json.dump() for writing and json.load() for reading.

import json
# Python dictionary
data = {'name': 'John Doe', 'age': 30, 'city': 'New York'}
# Writing Python dictionary to a JSON file
with open('data.json', 'w') as file:
    json.dump(data, file)
# Reading JSON data from a file
with open('data.json', 'r') as file:
    loaded_data = json.load(file)
# Accessing loaded data
print(f"Name: {loaded_data['name']}, Age: {loaded_data['age']}, City: {loaded_data['city']}")