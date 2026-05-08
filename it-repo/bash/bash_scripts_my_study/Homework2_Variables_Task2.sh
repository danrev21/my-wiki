# Run following script and fix errors
vi fixed.sh
#   #!/bin/bash
#   var1='Hello, '
#   var2="broken "
#   var3="script!"
#   printf '%b' "$var1" "$var2" "$var3\n"
chmod u+x fixed.sh
./fixed.sh

# Example of corrected output:
#   ./fixed.sh
#   Hello, broken script!