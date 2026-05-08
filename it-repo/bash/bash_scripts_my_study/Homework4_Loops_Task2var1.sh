# Develop simple script which will be print numbers 
# in range from 20 to -20 with step=4. 
# (Hint: try to use echo {80..100}; echo {80..100..3})
# Expected output: 20 16 12 8 4 0 -4 -8 -12 -16 -20
cat ./double20.sh
#!/bin/bash
for i in $(echo {20..0});
do
   p=$[ $i % 4 ]
   if [ $p -eq "0" ]
     then echo -n " "$i
   fi
done
echo -n " "
echo {-4..-20..4}