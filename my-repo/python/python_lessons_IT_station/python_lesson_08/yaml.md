# pyyaml Module: Parsing and Generating YAML**

---------------------------------------------------------------------------
# Parsing YAML Data: To parse YAML data, you can use the yaml.load() function provided by the pyyaml module.

import yaml
# YAML data as a string
yaml_data = """
name: John Doe
age: 30
city: New York
"""
# Parsing YAML data
data = yaml.load(yaml_data, Loader=yaml.FullLoader)
# Accessing data
print(f"Name: {data['name']}, Age: {data['age']}, City: {data['city']}")

----------------------------------------------------------------------------
# Generating YAML Documents: To create YAML documents, you can use the yaml.dump() function.
# This example converts a Python dictionary into a YAML document.

import yaml
# Python dictionary
data = {'name': 'Jane Smith', 'age': 25, 'city': 'San Francisco'}
# Generating YAML document
yaml_document = yaml.dump(data)
# Printing the YAML document
print(yaml_document)

--------------------------------------------------------------------------------
# Handling YAML Files: pyyaml simplifies working with YAML files. You can read YAML data from a file using yaml.safe_load() and write YAML data to a file using yaml.dump().

import yaml
# Reading YAML data from a file
with open('data.yaml', 'r') as file:
    data = yaml.safe_load(file)
# Modifying the data
data['age'] = 31
# Writing YAML data to a file
with open('data_updated.yaml', 'w') as file:
    yaml.dump(data, file)





