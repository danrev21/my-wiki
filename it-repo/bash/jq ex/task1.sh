#!/bin/bash

awk 'BEGIN{FS=OFS=","} {NF=NF-2}'1 accounts.csv |
        tail -n +2 |  sed -e "s/\b\(.\)/\u\1/g" |
        sed 's/,,,*/,/g' | sed 's/"*//g' > accounts_edit.csv
awk -F "," '{print $3}' accounts_edit.csv | awk -F " " '{print $1}' | sed 's/[^,]*/\l&/g' | cut -c1-1 > letter_email.csv
awk -F "," '{print $3}' accounts_edit.csv | awk -F " " '{print $2}' | sed 's/[^,]*/\l&/g' > surname_email.csv
awk -F "," '{$5=$2"@abc.com"} {print $5}' accounts_edit.csv > domain_email.csv
paste -d, letter_email.csv surname_email.csv domain_email.csv | sed 's/,//g' > email.csv
paste -d, accounts_edit.csv email.csv > accounts_edit2.csv
cat accounts_edit2.csv
p=($(awk -F "," '{print $3}' accounts_edit.csv | nl | sort -k2 | uniq -D -f1 | cut -f1))  # > repeat.csv


# awk -F ',' '$3  '{$5="GOOOOOAAAAL"} {print $1 "," $2 "," $3 "," $4 "," $5 ","}' accounts.csv
# sed 's/[0-9]*//g'  #удаление индекса из имейла
# echo ${r[@]} 
# sed '1i\id,location_id,name,title,email,' | # добавление заголовка таблицы
#   tmp && mv tmp "$file"