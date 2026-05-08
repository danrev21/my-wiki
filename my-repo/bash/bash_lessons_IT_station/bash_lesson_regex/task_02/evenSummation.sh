# Receive an unordered set of numbers through a script. 
# Design a program to display the total of all even figures within this set.

# Instructions:
# Given an unarranged series of digits provided to the script, 
# the task is to compute and showcase the collective sum of numbers that are even.

# Sample Execution:
# ./evenSummation.sh "1,2,3,4,5,6,7"
# Displayed Output: 12

#!/bin/bash 

# find only even digits
# /^[0-9]*[13579]$/d - regex of all odd numbers
arr=$(echo $1 | sed 's/,/\n/g' | sed '/^[0-9]*[13579]$/d')
# summing up the elements of the resulting array
for d in ${arr[@]}; do
    sum=$((sum + d))  
done
echo $sum
