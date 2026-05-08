# Develop simple script which will be print numbers 
# in range from 20 to -20 with step=4. 
# (Hint: try to use echo {80..100}; echo {80..100..3})
# Expected output:
./double20.sh
 20 16 12 8 4 0 -4 -8 -12 -16 -20
#!/bin/bash
for i in $(echo {80..100});
do
   y=$((i-80))
   p=$[ $y % 4 ]
   if [ $p -eq "0" ]
     then o="$y $o"
   fi
done
echo "$o"