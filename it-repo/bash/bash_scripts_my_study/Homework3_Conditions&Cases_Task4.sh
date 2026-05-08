# Write a script that executes the command cat /etc/shadow. 
# If the command return a 0 exit status, report Command succeeded and exit with a 0 exit status. 
# If the command returns a non-zero exit status, report Command failed and exit with a 1 exit status.
vi 03-get-shadow.sh
#   #!/bin/bash
#   cat /etc/shadow
#   if [ $? -ne 0 ] ;
#       then echo -e "Command failed \nExit status-$?" ;
#       else echo -e "Command succeeded \nExit status-$?" ;
#   fi
cat 03-get-shadow.sh
./03-get-shadow.sh
# Command failed...
sudo ./03-get-shadow.sh
# Command succeeded...