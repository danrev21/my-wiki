# Script should print maximum number from generated list
# Script should print minimal number from generated list
# Script should print sum of all generated numbers
cat elements.sh
#   #!/bin/bash
#   function rand() {
#       echo $(($RANDOM % ${1}))
#   }
#   for item in `seq 1 10`
#   do
#       value="$(rand 100)"
#       echo "[$item] => ${value}"
#   done
## write your code here ##

#!/bin/bash
function rand() {
echo $(($RANDOM % ${1}))
}
for item in `seq 1 10`; do
   value="$(rand 100)"
   echo "[$item] => ${value}"
done > result
cat result
 echo "min=$(cat result | awk '{ print $3 }' | sort -rn | tail -n1)"
 echo "max=$(cat result | awk '{ print $3 }' | sort -rn | head -n1)"
 r=($(cat result | awk '{ print $3 }'))
  t=0
  for i in ${r[@]}; do
    let t+=$i
  done
 echo "sum=$t"