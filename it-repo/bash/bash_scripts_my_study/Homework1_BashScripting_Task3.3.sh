# You’re given a file with the content (see below). Using sed perform:
    # remove all lines with word Linux
    # replace first appearance word xterm to word Bash
    # (extra) try to combine two tasks above in one-line command
touch sed_task && cat > sed_task
# CentOS is a Linux distribution that provides a free, community-supported computing platform functionally compatible with its upstream source, Red Hat Enterprise Linux (RHEL).
# GNU xterm or simply Bash is a Unix shell and command language written by Brian Fox for the GNU Project as a free software replacement for the Bourne shell.
# Linux is a family of open source Unix-like operating systems based on the Linux kernel.
sed -i '/Linux/d; s/xterm/Bash/g' sed_task
cat sed_task