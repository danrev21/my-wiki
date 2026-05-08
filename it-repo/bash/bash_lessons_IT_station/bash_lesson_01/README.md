
HOME TASKS
---------
Task 00 - Stream Handling in Bash
---------------------------------
Objective: Understand the difference between Standard Output (stdout) and Standard Error (stderr) in Bash. Learn to redirect these streams to different files and also how to silence them.

Task Steps:
-----------
Script Creation:

Develop an executable script named fd.sh. Incorporate the below code into this script:

echo "This is a standard output"

echo "This is an error message" >&2

exit 0

Output Redirection:
-------------------
Execute the fd.sh script you just created.
As the script produces both stdout and stderr, we want to redirect these streams to separate files.
Redirect the stdout to a file named stdout.txt.
Redirect the stderr to another file named stderr.txt.

Silencing Streams: Create another script named fd2.sh with the following contents:
----------------------------------------------------------------------------------

#!/usr/bin/env bash

echo "This is a standard output that will be silenced" 

echo "This is an error message that will be silenced" >&2

exit 0

When you run this script, ensure both stdout and stderr are silenced. This means their contents should be directed to /dev/null.

Tips:
----
Remember the importance of file permissions. Make sure your scripts are executable before running them.
Understand the difference between > and 2>. One redirects stdout and the other stderr.
The /dev/null is a special file that discards all the data written to it (and provides no data to any process that reads from it).


Task 01 - File Checking and Operation
------------------------------------
Task Details:
------------
Name the script check_files.sh.
Your script should check if the file named data.txt exists in the current directory.

If data.txt is found:
Print the message "File data.txt found!"
Make a backup of data.txt and name the backup file backup.txt.

If data.txt is not found:
Print the message "File data.txt not found!"

Hint:
-----
You can use the combination of && and || to perform the required actions based on the result of the file check.

test:
-----
Run the script in a directory containing data.txt:

./check_files.sh
File data.txt found!


