# Develop simple script which will be execute infinite 
# while loop with reading input in variable (etc. var) (read command) 
# and outputting message Hello ${var}. The has been ended when we enter word stop
# Expected output: ./04-infinite.sh
#                   Andrey
#                   Hello, Andrey
#                   Aliens
#                   Hello, Aliens
#                   stop
cat ./04-infinite.sh
#!/bin/bash
while true; do
   read name
   if [ "$name" == stop ]; then break
   else echo "Hello, $name"; fi
done
./04-infinite.sh


