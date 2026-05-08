#!/bin/bash

# Your task is to write a Bash script that determines the type 
# of a triangle based on its three sides.
# Script Name: triangle.sh.
# Input: The script should take three integer arguments, 
#   each representing one side of a triangle (X, Y, and Z).
# Output: If all three sides are equal, the script should 
#   output EQUILATERAL. If exactly two sides are equal 
#   (and one is different), the script should output ISOSCELES.
#   If no sides are equal, the script should output SCALENE.
# Constraints: The side lengths are represented by integers with 
# values between 1 and 100, inclusive. (i.e., 1 <= X, Y, Z <= 100)
# Hints: Use conditional statements to compare the three side 
# lengths and determine the type of the triangle.
# Check: Test your script with the following inputs and ensure it 
# produces the expected outputs:
# ./triangle.sh 2 3 4  
# Expected Output: SCALENE
# ./triangle.sh 6 6 6 
# Expected Output: EQUILATERAL

# Matching arguments to regex positive integer between 1 and 100:
for arg in $@
  do
    if [[ ! $arg =~ ^[1-9][0-9]?$|^100$ ]]; then
      echo "Input is wrong. Only positive integer between 1 and 100. Restart script."; exit
    fi
  done

# or this way:
#if [[ ! $1 =~ ^[1-9][0-9]?$|^100$ ]] || [[ ! $2 =~ ^[1-9][0-9]?$|^100$ ]] || [[ ! $3 =~ ^[1-9][0-9]?$|^100$ ]];
#   then echo "Input is wrong. Restart script."; exit;
#fi

# Checking triangle type:
if [[ $1 -ne $2 ]] && [[ $1 -ne $3 ]] && [[ $2 -ne $3 ]];
   then echo "SCALENE";
elif [[ $1 -eq $2 ]] && [[ $1 -eq $3 ]] && [[ $2 -eq $3 ]];
   then echo "EQUILATERAL";
   else echo "ISOSCELES";
fi
