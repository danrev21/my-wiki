#!/bin/bash

# Create new accounts_new.csv file based on current accounts.csv.
# Name format: first letter of name/surname uppercase and all other letters lowercase.
# Need to update column email with domain @abc.
# Email format: first letter from name and full surname, lowercase.
# Equals emails should contain location_id.

# deleting the title, first letters in uppercase, deleting ""
cat $1 | tail -n +2 | sed -e "s/\b\(.\)/\u\1/g" | sed 's/"*//g' > out1.csv
# create 'department' column
awk -F "," '{print $1 "," $2 "," $3 "," $4 "," $5 "," $6}' out1.csv > out2.csv
awk -F "," '$5 ~ /.+@.+/ {$5=""}{print $1 "," $2 "," $3 "," $4 "," $5 "," $6 ","}' out2.csv | # delete old email only in 'email' column
    awk -F "," '$5 ~ /.+/ {$6=$5}{print $6}' | awk '{$1=$1;print}' > department.csv # copy department data from 'email' to 'department' and saving
# create base file for next transformations
awk -F "," '{print $1 "," $2 "," $3 "," $4}' out1.csv > accounts_edit.csv

# preparing files for the destination table
awk -F "," '{print $3}' accounts_edit.csv | awk -F " " '{print $1}' | tr 'A-Z' 'a-z' | cut -c1-1 > letter_email.csv # the first letter of the name    
awk -F "," '{print $3}' accounts_edit.csv | awk -F " " '{print $2}' | tr 'A-Z' 'a-z' > surname_email.csv # surname
awk -F "," '{print $2"@abc.com"}' accounts_edit.csv > domain_email.csv # domain name email with id_location
awk -F "," '{print "@abc.com"}' accounts_edit.csv > domain_email_noid.csv # domain name email without id_location
paste -d, letter_email.csv surname_email.csv domain_email.csv | sed 's/,//g' > email_id.csv # iivanov5@abc.com (id_location)
paste -d, letter_email.csv surname_email.csv domain_email_noid.csv | sed 's/,//g' > email_noid.csv # iivanov@abc.com (no id_location)      
paste -d, accounts_edit.csv email_id.csv department.csv > accounts_allid.csv # list of employees with id_location in email
paste -d, accounts_edit.csv email_noid.csv department.csv > accounts_allnoid.csv # list of employees no id_location in email

# creating a list of employees with id_location (with the same names)
awk -F "," '{print $3}' accounts_edit.csv | nl | sort -k2 | uniq -D -f1 | cut -f1 > repeat.csv # line numbers of matching names (with id_loc)
mapfile -t arr < repeat.csv
for n in ${arr[@]}; do
   awk -v n="$n" 'FNR==n' accounts_allid.csv;
done > accounts1.csv # writing a list of employees with id_location to a preliminary destination file

# creating a list of employees no id_location
awk -F "," '{print $1}' accounts_edit.csv > num.csv
> differ.csv
while read -r line; do
    df=$(awk -F, '{print tolower($NF)}' <<< "$line")
    if [[ ! " ${arr[@]} " =~ " $df " ]]; then
       echo "$line" >> differ.csv # line numbers with mismatched names (no id_location)
    fi
done < num.csv

# comparison of mismatches and list of employees no id_location
mapfile -t differ < differ.csv
for m in ${differ[@]}; do
   awk -v m="$m" 'FNR==m' accounts_allnoid.csv;
done >> accounts1.csv # writing a list of employees no id_location to a preliminary destination file

# creating the final file
cat accounts1.csv | sort -nk1 | sed '1i\id,location_id,name,title,email,department' > accounts_new.csv
cat accounts_new.csv
echo -e "\nFile is ready."

# remove tmp files
rm out1.csv out2.csv department.csv accounts_edit.csv letter_email.csv surname_email.csv domain_email.csv domain_email_noid.csv num.csv email_id.csv email_noid.csv accounts_allid.csv accounts_allnoid.csv differ.csv repeat.csv accounts1.csv


# ./task1.sh accounts.csv