#!/usr/bin/env python

# Calculating Factorial Recursively:

def factorial(n):
    """
    Calculate the factorial of a number using recursion.
    :param n: The number for which to calculate the factorial.
    :return: The factorial of n.
    """
    if n == 0:
        return 1  # Base case
    else:
        return n * factorial(n - 1)  # Recursive case

result = factorial(5)
print(result)

########################################################
# simple recursion function
def Recursion(i):
  print(i)
  if i == 1:
    return i
  else:
    Recursion(i-1)

Recursion(5)
# output:
# 5
# 4
# 3
# 2
# 1
######################################################
# return even numbers before specified number

def EvenNums(num):
    print(num)
    if num % 2 != 0:
        print("Please enter even number!")
    elif num == 2:
        return num
    else:
        return EvenNums(num - 2)
    
EvenNums(8)
# output:
# 8
# 6
# 4
# 2
 