#!/usr/bin/env python

def deco(func):
  def wrapper():
    print("start wrapper")
    func()
    print("end wrapper")
  return wrapper

@deco
def test():
  print("run test func")

if __name__=="__main__":
  test()