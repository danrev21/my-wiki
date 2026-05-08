#!/usr/bin/env python


fruits = ['apple', 'banana', 'orange']

fruits.append('grape')
print(fruits)         # output: ['apple', 'banana', 'orange', 'grape']
fruits.extend(['kiwi', 'melon'])
print(fruits)         # output: ['apple', 'banana', 'orange', 'grape', 'kiwi', 'melon']
fruits.insert(1, 'pear')
print(fruits)         # output: ['apple', 'pear', 'banana', 'orange', 'grape', 'kiwi', 'melon']
fruits.remove('banana')
print(fruits)         # output: ['apple', 'pear', 'orange', 'grape', 'kiwi', 'melon']
fruits.pop(2)
print(fruits)         # output: ['apple', 'pear', 'grape', 'kiwi', 'melon']