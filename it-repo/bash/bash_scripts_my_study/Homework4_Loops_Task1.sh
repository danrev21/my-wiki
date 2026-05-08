# Develop simple script which will be print numbers in range from 1 to 10. 
# (Hint: try to use seq 10 20 with different options)
# Expected output:
./seq10.sh
 1 2 3 4 5 6 7 8 9 10
#!/bin/bash

for n in `seq 10 20`
do
   echo $((r=n - 9))
done | sed '$d' | paste -sd " "
