#!/bin/bash

echo "PS1='\[\e]0;\u@\h: \w\a\]${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;35m\]\w\[\033[00m\]\$'" >> .bashrc
bash

sudo useradd -mG sudo -p $(perl -e 'print crypt($ARGV[0], "password")' 4563) -s /bin/bash ben

sudo apt update -y

sudo apt install vim net-tools tree ncdu bash-completion curl dnsutils htop iftop pwgen screen sudo wget -y

sudo apt install fail2ban -y

sudo ufw allow OpenSSH
echo y | sudo ufw enable



