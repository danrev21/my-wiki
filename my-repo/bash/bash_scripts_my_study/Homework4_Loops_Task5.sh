# Let’s develop a simple console game! You’re given a script template (see below). Append script which will be:
# At the beginning of the game script randomly sets Magic number
# User is running script and trying to guess magic number: if entered number less than magic number, script outputs less; if entered number greater than magic number, script outputs greater; if user have guessed the magic number, script outputs You win!
# Expected output: ./03-magic-number.sh
#                   10
#                   less
#                   20
#                   greater
#                   15
#                   You win!
cat 03-magic-number.sh
#!/bin/bash
magicNumber=$(( $RANDOM % 100 ))
echo "Guess the number from 1 to 100:"
while true; do
   read x
   if [ "$x" -lt "$magicNumber" ]; then echo "greater"
   elif [ "$x" -gt "$magicNumber" ]; then echo "less"
   else echo "You win!"; break; fi
done
./03-magic-number.sh