#   Need to parce output.txt to convert into output.json:
#   1. Count of tests can be more than 2
#   2. Rating is a number and can be float or int (for example 50.23, 50, 100)
#   3. Sripts should has name task2.sh
#   4. Path to output.txt file should be as argument to the script.

#!/bin/bash

# удаление пустых строк во входном файле
cat $1 | sed '/^$/d' | sed -r 's/^[0-9]+.+/;/g' > out1.txt
cat /dev/null > out.txt
IFS=$';'
for var in $(cat out1.txt)
    do
        
        ((++j))
        echo "$var" > file$j.txt
        
        cat file$j.txt | sed '/^$/d' | head -n1 | sed 's/.*\[//;s/\].*//' | awk '{$1=$1};1' > headfile$j.txt
        # parsing headfile.txt;
        cat headfile$j.txt | jq --slurp --raw-input --raw-output 'split("\n") | .[0:] | map(split(",")) | map({"testName": .[0], "tests":.[1]})' |
                sed -e 's/[][?!]//g' -e 's/^[ \s]*//;s/[ \s]*$//' |    # delete []; delete spaces at the beginning and end 
                        sed -r 's/("tests": ).*/\1/g' | sed -z '$ s/^\n// ; $ s/...\n$//' >> out.txt   # removing "null" and line feed

        # step of test; deleting the first and last lines; lines "-"; deleting test numbers; replacing "," with ";" (leave "," in ()), deleting spaces
        cat file$j.txt | sed -e '/^$/d' -e '1d' -e '/-/d' -e 's/not ok/false,/g' -e 's/ok/true,/g' -re 's/\s[0-9]+\s//g' -re 's/,\s+([^.]*),\s/;\1;/g' |
        awk '{$1=$1};1' > testsfile$j.txt

        # parsing test.txt
        cat testsfile$j.txt |
        jq --slurp --raw-input --raw-output 'split("\n") | .[0:] | map(split(";")) | map({"name": .[1], "status": .[0]|fromjson, "duration": .[2]})' |
            sed -e '$ s/.$/&\,/' >> out.txt   # adding "," to the end of the last line

        # summary data
        failed=$(cat testsfile$j.txt | awk -F';' '{ print $1 }' | grep -o 'false' | wc -w)   # failed
        success=$(cat testsfile$j.txt | awk -F';' '{ print $1 }' | grep -o 'true' | wc -w)   # true
        rating=$(echo "scale=2;$success * 100/($success + $failed)" | bc)   # rating
        duration=$(cat testsfile$j.txt | sed 's/[A-z]*//g' | awk -F ';' '{sum+=$3;} END { print sum }')   # duration
        # parsing summary data
        echo '{"summary":{"success": '$success',"failed": '$failed',"rating": '$rating',"duration":"'$duration'ms"}}' | jq . > tailfile$j.txt
        # deleting the first "{" ; deleting spaces at the beginning of all lines; deleting the first \n
        cat tailfile$j.txt | sed 's/^{//g' | sed 's/^\s.//' | sed -z 's/^\n//' >> out.txt
        rm file$j.txt headfile$j.txt testsfile$j.txt tailfile$j.txt
done
# output file
jq '.' out.txt > output.json
jq '.' output.json
rm out.txt out1.txt

# ./task2.sh output.txt