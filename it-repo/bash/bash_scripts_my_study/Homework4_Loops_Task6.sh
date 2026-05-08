# You’re given the file with varied paths. 
# Depend on existing “/” at the end of each line create regular file (path without ‘/’) 
# or directory (path with / at the end) with given path.
# Expected output:  cat paths | ./04-create-items.sh
#                   ls –l /tmp
#                   /tmp/dir1/
#                   /tmp/dir3/
#                   /tmp/file1
#                   /tmp/file2
#                   ...
cat paths
/tmp/file1
/tmp/file2
/tmp/dir1/
/tmp/dir3/
/tmp/dir3/file3
cat ./04-create-items.sh

if [[ $# == "*/" ]]; then
