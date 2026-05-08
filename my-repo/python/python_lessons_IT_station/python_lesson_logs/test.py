#!/usr/bin/env python

################   T   E   S   T   #########################

import re
import sys
# '192.168.56.4 - - [14/Nov/2023:03:11:42 +0000] "GET / HTTP/1.1" 200 10926 "-" "curl/7.81.0"'

line_regex = re.compile(r'''(?P<remote_host>\S+) #ip ADDRESS
                              \s+ #whitespace
                              \S+ #remote logname
                              \s+ #whitespace
                              \S+ #remote user
                              \s+ #whitespace
                              \[(?P<Time>.*) \+\d{4}\] #time
                              \s+ #whitespace
                              "[^"]+" #first line of request
                              \s+ #whitespace
                              (?P<status>\d+)
                              \s+ #whitespace
                              (?P<bytes_sent>-|\d+)
                              \s* #whitespace
                              \S+\s+# "-" + whitespace
                              "(?P<agent>.*)"
                              ''', re.VERBOSE)
def split_line(line):
    return line_regex.match(line).groupdict()

if __name__ == "__main__":
    ip_addresses = []
    with open("./apache_logs/access.log") as log:
        for line in log.readlines():
            splited_line = split_line(line)
            ip_address = splited_line["remote_host"]
            if ip_address not in ip_addresses:
                ip_addresses.append(ip_address)
    print(ip_addresses)
     