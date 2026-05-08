#!/usr/bin/env python

# https://www.w3schools.com/python/python_strings.asp

sentence = "   Python Programming is FUN!   "
length = len(sentence)
lower_case = sentence.lower()
upper_case = sentence.upper()
stripped_sentence = sentence.strip()
words = sentence.split()
joined_sentence = ' '.join(words)

print(length)             # Output: 32
print(lower_case)         # Output: "   python programming is fun!   "
print(upper_case)   # Output: "PYTHON PROGRAMMING IS FUN!   "
print(stripped_sentence)  # Output: "Python Programming is FUN!"
print(words)              # Output: ['Python', 'Programming', 'is', 'FUN!']
print(joined_sentence)    # Output: "Python Programming is FUN!"