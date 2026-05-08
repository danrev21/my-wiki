# Develop “User Info” Script
mkdir work && cd /work
vi user-info.sh
    # #!/bin/bash
    # echo Home dir: $HOME
    # echo User Name: $USER
    # echo User ID: $UID'('$USER')'
    # echo Group Information: `id | awk '{print $2}' | cut -d'=' -f2`
    # echo Terminal: $TERM
    # echo Current directory: `pwd`
    # echo System date/time: `date`
chmod u+x user-info.sh
./user-info.sh
echo $?