# output hello variable with replacement word hello->goodbye with one-line command
hello="Hello world!"
echo ${hello//Hello/Goodbye}
Goodbye world!