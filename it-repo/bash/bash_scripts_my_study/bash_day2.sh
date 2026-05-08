#!/bin/bash 

# Day 3 BASH 
# 1. Create new branch <name>_<surname>_bash2. 
# 2. Create a script bash_day2.sh in ./03_BASH/ folder. 
# 3. Script should be executable with /bin/bash. 
# 4. Script should do the following: 
 
# d. Create function makefile that takes two arguments (size, filename) 
#and creates file $filename of $size size in current directory 
function makefile () { 
        SIZE=$1 
        NAME=$2 
        SIZE="$SIZE"MiB 
        echo "Size: $SIZE File: $NAME" 
        truncate -s "$SIZE" "$NAME" 
} 

# a. NAME_SURNAME variable passed as an argument to the script. 
# For example: ./bash_day2.sh Walter_White 
NAME_SURNAME=$1 
SURNAME=$(echo "$NAME_SURNAME" | cut -d '_' -f2) 
 
# b. Have ARRAY array variable containing letters of your surname 
declare -a ARRAY 
 
# e. Create any loop that iterates over SURNAME variable excluding the last 
# element and calls makefile function passing loop (index + 1) as size in megabytes(M) 
# and array element as filename to create files in SURNAME folder. For example: 
# if SURNAME=White 4 files should be created with: W - 1M; h - 2M and etc. 
for ((i=0; i<=${#SURNAME}-1; i++)) 
do 
   ARRAY=( "${ARRAY[@]}" "${SURNAME:$i:1}") 
done 
echo "ARRAY ${ARRAY[@]}" 
 
ARRAY_SIZE=${#ARRAY[@]} 
echo "ARRAY_SIZE $ARRAY_SIZE" 
 
# c. Create SURNAME folder in current directory ./ 

mkdir -p ./"$SURNAME" 
 
for ((i=0;  i<${#ARRAY[@]}-1; i++)) 
do 
   makefile $((i+1)) "$SURNAME/${ARRAY[${i}]}" 
done

# 5. Create length(SURNAME) * 2 folders named 1, 2, 3, 4, 5, … in 
# SURNAME folder. For example: if SURNAME=White then length=5 10 
# folders should be created. 
for ((i=1;  i<="$ARRAY_SIZE"*2; i++)) 
do 
        mkdir "$SURNAME"/"$i" 
done 

# 6. Create a command that runs the script above while redirecting 
# **ALL** output to `./log.log` file (write command as comment into script).

# bash ./bash_day2.sh Daniil_Tyuev > log.log 2>&1