sudo du -sh /var/lib/snapd


#!/bin/bash
 
#Removes old revisions of snaps
#CLOSE ALL SNAPS BEFORE RUNNING THIS
set -eu
LANG=en_US.UTF-8 snap list --all | awk '/disabled/{print $1, $3}' |
    while read snapname revision; do
        snap remove "$snapname" --revision="$revision"
    done
     
     
     
# chmod +x clean_snap.sh
# sudo  ./clean_snap.sh
