# Develop a script called 03-which-daemon.sh that checks if the httpd and init daemons are running on your system.
ps -ef | grep [h]ttpd
# apache   27906 29214  0 Sep29 ?    00:00:00 /usr/sbin/httpd -DFOREGROUND
# root     29214     1  0 Sep27 ?    00:00:35 /usr/sbin/httpd -DFOREGROUND
vi 03-which-daemon.sh
#   #!/bin/bash
#   p=$(ps -ef | grep [h]ttpd)
#   case "$p" in
#      *[h]ttpd*) echo "This machine is running a web server."
#      ;;
#   esac
cat 03-which-daemon.sh
./03-which-daemon.sh
# This machine is running a web server.