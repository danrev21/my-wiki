=================================================
# setup PATH for own script run from any directory

env | grep PATH

mkdir example
vim example/example.sh

    #!/bin/bash
    
    echo "Hello World!"

chmod +x example/example.sh
export PATH=/home/vagrant/example:PATH

# now you can run this script from any directory