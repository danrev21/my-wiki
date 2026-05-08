#!/usr/bin/env python

# Writing to a file
with open("file.txt", "w") as file:
    file.write("Hello, Python!\n")


#!/usr/bin/env python

# script writes lines in file
with open('file.txt', 'a') as file:
    l1 = "Welcome to TutorialsPoint\n"
    l2 = "Write multiple lines \n"
    l3 = "Done successfully\n"
    l4 = "Thank You!"
    file.writelines([l1, l2, l3, l4])
file.close()

