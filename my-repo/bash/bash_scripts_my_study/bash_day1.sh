#!/bin/bash 

# Day 2 BASH 
# 0. Create new branch <name>_<surname>_bash1. 
# 1. Create a script bash_day1.sh in ./02_BASH/ folder. 
# 2. Script should be executable with /bin/bash. 

# 3. Make NAME, SURNAME and FAIL named arguments (-n, -s, -f) 
# 4. Script should not stop execution if it encounters errors. 
# 5. Script should be able to run many times without errors. 
# 6. Script should do the following: 
#   a. Have NAME and SURNAME variables (values are your name and surname) 
#   b. Have FAIL variable 
NAME="dan" 
SURNAME="gusev" 
FAIL="fail" 
 
while getopts n:s:f: flag 
do 
        case "${flag}" in 
                n) NAME=${OPTARG};; 
                s) SURNAME=${OPTARG};; 
                f) FAIL=${OPTARG};; 
        esac 
done 
 
# c. Have ARRAY array variable containing letters of your surname 
declare -a ARRAY 
array_surname=${#SURNAME} 
for ((i=0; i<=$((array_surname-1)); i++)) 
do 
    ARRAY=( "${ARRAY[@]}" "${SURNAME:$i:1}") 
done 
 
# d. Create folder in current directory ./ and name it as NAME_SURNAME 
sldir="$NAME""_""$SURNAME" 
if ! [ -d "$sldir" ] 
then 
        mkdir "$sldir" 
fi 
cd "$sldir" 
 
# e. Create 3 files of the following sizes in NAME_SURNAME folder named after 
# ARRAY variable elements: 1st element(1KiB), 2nd element (1MiB), last element (10MiB). 
# Each file must have size that is specified in brackets. Sizes are specified 
# in KiB and MiB (1024 based). 
fst=${ARRAY[0]} 
snd=${ARRAY[1]}
last=${ARRAY[-1]} 
truncate -s 1K ./"$fst"
truncate -s 1M ./"$snd" 
truncate -s 10M ./"$last"

# f. Search current directory ./ for all files modified in last 1h and output those file(s) 
# names into your NAME_SURNAME folder into search.log file. 
cd .. 
find ./"$sldir" -mmin -60 -type f | xargs ls -l  >> ./"$sldir"/search.log 
 
# g. Create tarball with the name archive.tar with 1st and 2nd files from task 6.e. Save this 
# tarbal into your folder NAME_SURNAME. 
cd "${sldir}" 
if ! [ -f archive.tar ] 
then 
   touch archive.tar 
fi 
tar -cvf archive.tar "$fst" "$snd" 
 
# h. Append 3rd file created in task 6.e to archive.tar 
tar -rf archive.tar "$last" 
 
# i. Remove files created in task 6.e 
rm "$fst" "$snd" "$last" 
 
# j. Create ./unarchived folder and unarchive archive.tar into this folder 
cd .. 
if ! [ -d unarchived ] 
then 
    mkdir unarchived 
fi 
tar -C ./unarchived -xvf "${sldir}"/archive.tar 
 
# k. Exit with exit code 3 if FAIL=true, exit with exit code 2 if FAIL=false, 
# exit with exit code 0 if FAIL variable is not set 
case $FAIL in 
        true) exit 3; 
        ;; 
        false) exit 2; 
        ;; 
        0|null) exit 0; 
        ;; 
esac
