#!/bin/bash

# Your task is to create a Bash script that performs basic 
# arithmetic operations on two given numbers.

# Script Name: calculate.sh.
# Input: The script should accept two numeric arguments.
# Output: The script should calculate and display the:
#   Sum of the two numbers.
#   Product of the two numbers.
#   Quotient when the first number is divided by the second. (You can use integer division for simplicity.)
#   Difference between the first and the second number.
# All results should be printed to STDOUT.

# Hints:
# Remember to use basic arithmetic operators in Bash to perform these calculations.
# Check: Test your script with the following input and ensure it provides the expected output:

sum=$(($1 + $2))
dif=$(($1 - $2))
pro=$(($1 * $2))
quo=$(($1 / $2))

echo "Sum: $sum"
echo "Product: $pro"
echo "Quotient: $quo"
echo "Difference: $dif"
