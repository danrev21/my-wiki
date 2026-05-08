#!/bin/bash
#Day 1 SED/AWK
#EXTRA. Create new script sed_awk_extra.sh in 01_SED_AWK folder.
#Create copy of passwd file to passwd_extra. Do changes in items 3.b/3.c
#using bash only. (No sed, awk, vim and replace, just pure bash).
#3.b. Change shell for user saned from /usr/sbin/nologin to /bin/bash using AWK
#3.c. Change shell for user avahi from /usr/sbin/nologin to /bin/bash using SED
pf='./src/passwd'
pfe='./passwd_extra'
declare -a my_str
IFS=$'\n'

cp -f $pf $pfe

for file in $(cat $pfe)
do
        IFS=:
        my_str=($file)

        if [[ ${my_str[0]} == "saned" ]] || [[ ${my_str[0]} == "avahi"  ]]
        then
                my_str[6]="/bin/bash"
        fi

        collect+="${my_str[*]}"$'\n'
        IFS=$'\n'
done
echo "$collect" > $pfe
truncate -s -2 $pfe