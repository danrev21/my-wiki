# Using awk print usernames from /etc/passwd file.
cat /etc/passwd
cat /etc/passwd | awk -F":" '{print $1}'