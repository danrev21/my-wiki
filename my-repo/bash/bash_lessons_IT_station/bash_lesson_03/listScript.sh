#!/bin/bash

# Construct a program that accepts a digit (indicating the desired 
# number of directories up to 26) as input. 
# The program should then generate these directories 
# within the current working path using the naming scheme dir_<[a-z]>.
# For example:
# ./listScript.sh 5
# Result: 5 directories established: dir_a, dir_b, dir_c, dir_d, dir_e
# ./listScript.sh 1
# Result: 1 directory established: dir_a

if [ $1 -gt 26 ]; 
  then echo "Input is wrong. Restart script."
  exit
fi 
a=({a..z})  # the same record: a=(a b c d e f g h i j k l m n o p q r s t u v w x y z)
for (( i=0; i<$1; i++ ))
do
  mkdir dir_${a[$i]}
done
