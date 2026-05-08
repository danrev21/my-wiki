# you’re given a variable with some path. Get parent path using string manipulating
mypath=$(pwd)
echo ${mypath}
# /home/devops/test_folder
echo ${mypath/danre}
# or
echo ${mypath/%danre/}
# /home/devops