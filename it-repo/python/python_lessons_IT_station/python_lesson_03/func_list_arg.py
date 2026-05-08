#!/usr/bin/env python

# Passing a List as an Argument

def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    :param numbers: A list of numbers.
    :return: The average of the numbers.
    """
    total = sum(numbers)
    count = len(numbers)
    return total / count

data = [10, 20, 30, 40, 50]
avg = calculate_average(data)
print(avg)