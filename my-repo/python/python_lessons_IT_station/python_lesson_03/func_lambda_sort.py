"""
lambda functions, also known as anonymous functions, 
are small, inline functions that can be used for 
simple operations. 
"""

# example 1
a = lambda x, y, z: x + y + z
print(a(1, 2, 3))  # output: 6


# example 2
names = ["Alice", "Bob", "Charlie", "David", "Eve"]

# Sorting names based on their length 
# using a lambda function
sorted_names = sorted(names, key=lambda x: len(x))
print(sorted_names)
# output: ['Bob', 'Eve', 'Alice', 'David', 'Charlie']