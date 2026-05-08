#!/usr/bin/env python

# to run: ./parse_with_re.py ./apache_logs/access.log

import re
import sys

line_regex = re.compile(r'''(?P<remote_host>\S+) #ip ADDRESS
                              \s+ #whitespace
                              \S+ #remote logname
                              \s+ #whitespace
                              \S+ #remote user
                              \s+ #whitespace
                              \[(?P<Time>.+)\s+\+\d*\] #time
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
    log_file = sys.argv[1]
    ip_addresses = []
    with open(log_file) as log:
        for line in log.readlines():
            splited_line = split_line(line)
            ip_address = splited_line["remote_host"]
            if ip_address not in ip_addresses:
                ip_addresses.append(ip_address)
    print(ip_addresses)
     