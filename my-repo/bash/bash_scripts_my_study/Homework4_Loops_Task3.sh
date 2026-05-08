# You are given an array of numbers. Using only one loop perform the following tasks:
# Print only even numbers
# Don't print numbers in range [30, 60]
# Stop loop executing when number will be greater than 85
# Expected output:
cat 04-numbers.sh
#!/bin/bash
array=$(seq 1 100)
for item in ${array}; do
  if (("$item" < "30"))  || (("$item" > "60")); then
    case $item in
      86) break ;;
    esac
    p=$[ $item % 2 ]
    if [ $p -eq "0" ]; then
      echo "$item"
    fi
  fi
done
./04-numbers.sh
2
4
6
...