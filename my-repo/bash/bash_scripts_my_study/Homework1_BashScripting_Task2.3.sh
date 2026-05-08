vi hello-something-wrong-3.sh
cat ./hello-something-wrong-3.sh
 # !/bin/bash
 #
 # echo Hello World!
chmod 644 hello-something-wrong-3.sh
ls –la ./hello-something-wrong-3.sh
# -rw-r--r-- 1 devops devops 32 Sep 30 08:38 ./hello-something-wrong-3.sh
chmod u+x hello-something-wrong-3.sh
./hello-something-wrong-3.sh