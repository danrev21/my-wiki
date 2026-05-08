# Do the same (task1), using a case statement and an alternative use of the date command.
vi month-days_2.sh
#   #!/bin/bash
#   N=$(date +%m)
#   leanYearMonths=(31 28 31 30 31 30 31 31 30 31 30 31)
#   for n in ${!leanYearMonths[@]}; do
#     case $n in
#      $N)
#      echo ${leanYearMonths[n-1]}
#      ;;
#     esac
#   done
./month-days_2.sh