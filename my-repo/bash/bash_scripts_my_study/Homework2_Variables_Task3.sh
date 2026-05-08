# Write a shell script which prints out value of global variable MY_VAR: 
export MY_VAR=my_value
vi global.sh
#   #!/bin/bash
#   echo 'MY_VAR='${MY_VAR-'default'}
./global.sh
# MY_VAR=my_value
MY_VAR=my_value ./global.sh 
# MY_VAR=my_value
unset MY_VAR  # reset variable
./global.sh
# MY_VAR=default