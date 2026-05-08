#!/usr/bin/env python

def deco(func):
  def wrapper(*args, **kwargs):
    print("start wrapper")
    return_value = func(*args, **kwargs)
    print("return value: {}".format(return_value))
    print("end wrapper")
    return return_value
  return wrapper

@deco
def test(x):
  return x * 2

print(test(2))