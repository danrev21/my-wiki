#!/bin/bash

# Script that can intelligently convert temperatures between Celsius and Kelvin scales.
# Input:
# The tool should be designed to accept a temperature figure, succeeded by its respective 
# measure (C signifies Celsius, K for Kelvin). For example, 25C or 298K.
# Conversion Logic:
# If the input is in Celsius, the script should return the value in Kelvins.
# If the input is in Kelvins, the script should return the value in Celsius.
# Utilize the following relationships:
# Celsius from Kelvin: C=K−273
# Kelvin from Celsius: K=C+273
# Output:
# The script should print the converted temperature value followed by its unit.
# Error Handling: Your script should be able to identify and alert the user if they provide:
# 1.Inputs that aren't numerical.
# 2.Entries lacking a definitive scale (either C or K absent).
# 3.Entries that suggest temperatures beneath the absolute zero threshold for the specified scale.
# Demonstration:
# ./temperature_transition.sh 55C
# Output Display: 328K

t=$(echo $1 | sed 's/[cCkK]//g')
case $1 in
    [0-9]*[^cCkK])
        echo "Scale is except. Try again."
	exit 1
    ;;
    -[0-9]*[^cCkK])
        echo "Scale is except. Try again."
	exit 1
    ;;
    [0-9]*[cC])
	[[ $t -lt -273 ]] 2> /dev/null && echo "Min value of absolute zero is -273C. Try again." && exit 1    
        echo "$((${1%[a-zA-Z]} + 273))K"
    ;;
    -[0-9]*[cC])
	[[ $t -lt -273 ]] 2> /dev/null && echo "Min value of absolute zero is -273C. Try again." && exit 1
        echo "$((${1%[a-zA-Z]} + 273))K"
    ;;
    [0-9]*[kK])
	[[ $t -lt -273 ]] 2> /dev/null && echo "Min value of absolute zero is -273C. Try again." && exit 1
        echo "$((${1%[a-zA-Z]} - 273))C"
    ;;
    -[0-9]*[kK])
	[[ $t -lt -273 ]] 2> /dev/null && echo "Min value of absolute zero is -273C. Try again." && exit 1
        echo "$((${1%[a-zA-Z]} - 273))C"
    ;;
     *)
        echo "Input is not numerical. Try again."
        exit 1
esac








