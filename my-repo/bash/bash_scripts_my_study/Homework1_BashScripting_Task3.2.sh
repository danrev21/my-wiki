# Using cut print group names from /etc/group file.
cat /etc/group
cat /etc/group | cut -d: -f1