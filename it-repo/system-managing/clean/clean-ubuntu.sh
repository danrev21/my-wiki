# Ubuntu Clean

#!/bin/bash

sudo apt autoremove 
rm -rf ~/.cache/thumbnails/*
sudo apt-get clean

du -h ~/.cache/thumbnails
du -h /var/cache/apt
