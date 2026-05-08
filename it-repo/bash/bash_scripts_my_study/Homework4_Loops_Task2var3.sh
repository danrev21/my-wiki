# Develop simple script which will be print numbers 
# in range from 20 to -20 with step=4. 
# (Hint: try to use echo {80..100}; echo {80..100..3})
# Expected output: 20 16 12 8 4 0 -4 -8 -12 -16 -20
cat ./double20.sh
#!/bin/bash
a=$(echo {80..100})
b=$(echo {80..100..3})
for i in $a; do
   y=$((i-80))
   p=$[ $y % 4 ]
   if [ $p -eq "0" ]; then o="$y $o"; fi
done
for j in $b; do
   u=$((j-100))
   l="$u $l"
done
IFS=' ' read -a arr <<< "$l"
len=${#arr[*]}
for (( c=0, k=2; c<=$(( $len -1 )); c++, k++ )); do
   arr[$c]=$((${arr[$c]} - k))
done
echo $o${arr[@]:0:5}