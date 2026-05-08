#!/bin/bash

# The script should be named loops.sh.
# The script must accept a single argument: a string.
# The script should produce the reversed version of the input string.
# It must swap the case of each letter in the string,
# i.e., convert uppercase letters to lowercase and vice versa.
# Check:
# ./loops.sh "Hello Bash"  
# Output: HSAb OLLEh

s="$1"
string=${#s}
for (( i=$string-1; i>=0; i-- )); do
  revstr=$revstr${s:$i:1}
  res=$(echo $revstr | tr 'a-zA-Z' 'A-Za-z')
done
echo $res
