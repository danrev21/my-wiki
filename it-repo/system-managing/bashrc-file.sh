# Temporary settings, when you logout setting will be lost. 
export PS1='\[\e[0;32m\]\u@\h:\w\$ \[\e[0m\]'
# Color	Code
# Black	0;30
# Blue	0;34
# Green	0;32
# Cyan	0;36
# Red	0;31
# Purple	0;35
# Brown	0;33
# Blue	0;34
# Green	0;32
# Cyan	0;36
# Red	0;31
# Purple	0;35
# Brown	0;33
==============================================================
# Temporary settings, when you logout setting will be lost. 
export PS1="\[$(tput setaf 2)\]\u@\h:\w $ \[$(tput sgr0)\]"
# setaf 1:
# Color {code}	Color
# BLACK="tput setf 0"
# BLUE="tput setf 1"
# GREEN="tput setf 2"
# CYAN="tput setf 3"
# RED="tput setf 4"
# MAGENTA="tput setf 5"
# YELLOW="tput setf 6"
# WHITE="tput setf 7"
# RETURN="tput sgr0"
# BOLD="tput bold"
# REV="tput rev"
===============================================================
# To make it permanent you have to write it to a file that will
# be loaded at the beginning of a session, like the precedent .bashrc.
echo "PS1='\[\e]0;\u@\h: \w\a\]${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;35m\]\w\[\033[00m\]\$'" >> .bashrc
bash
