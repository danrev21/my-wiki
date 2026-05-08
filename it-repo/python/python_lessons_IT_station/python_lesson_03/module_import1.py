#!/usr/bin/env python

# При импортирвании происходит выполнение 
# скрипта, и если необходимо чтобы при импортировании 
# скрипт не выполнялся добавляем строки if...: print
# сохраняя отступы - функция в теле if


def add(a, b):
  """
  Add two numbers and return the result.
  :param a: The first number.
  :param b: The second number.
  :return: The sum of a and b.
  """
  return a + b

# Calling the add function and capturing the return value
#result = add(3, 5)
#print(f"The sum is {result}")

if __name__ == "__main__":
  print(__name__)   # выводит __main__, т.е. имя скрипта поменялось
  print(add(3,5))
  
"""
In Python, modules are collections of Python code 
that can be reused in different programs. Importing 
modules allows you to access functions, variables, 
and classes defined in those modules. 

import module_import
module_import.add??

import module_import as mod
mod.add?

from module_import import add
add??
add(2, 4)

from module_import import add as a
a??
a(4, 6)

"""