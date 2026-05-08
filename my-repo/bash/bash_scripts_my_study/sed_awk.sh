#!/bin/bash

# create files
cp src/passwd passwd_new
cp src/poem.txt poem_new.txt
# Change file passwd
cat passwd_new | awk 'BEGIN{FS=OFS=":"} /saned/ {$NF="/bin/bash"}{print $0}' | 
	sed -r -e 's/(^avahi:.*):.*$/\1:\/bin\/bash/g' | 
	    awk 'BEGIN{FS=OFS=":"} {print $1, $3, $5, $7}' | 
	        sed '/.*daemon.*/d' | 
	            awk 'BEGIN{FS=OFS=":"} $2 ~ /d*[02468]$/ {$NF="/bin/zsh"}{print $0}' | head -c -1 > passwd_new
# Change file poem.txt
cat poem_new.txt | sed -r 's/e{2,}/alala/g' | sed 's/.$/!/g' | sed '/^$/d' > poem_new.txt
