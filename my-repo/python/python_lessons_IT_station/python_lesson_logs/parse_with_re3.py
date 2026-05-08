#!/usr/bin/env python

# using function and re.compile
# выводит уникальные ip из логов
# to run script: ./parse_with_re3.py ./apache_logs/access.log

import re
import sys

ip_regex = re.compile(r'(?P<IP_ADDRESS>\d+\.\d+\.\d+\.\d+)')

def split_line(line):
    return ip_regex.match(line).groupdict()
if __name__ == "__main__":
    log_file = sys.argv[1]
    ip_addresses = []
    with open(log_file) as log:
        for line in log.readlines():
            splited_line = split_line(line)
            print(splited_line)
            ip_address = splited_line["IP_ADDRESS"]
            if ip_address not in ip_addresses:
                ip_addresses.append(ip_address)
    
    print(ip_addresses)
     
# output: 
# ....
# {'IP_ADDRESS': '192.168.56.1'}
# {'IP_ADDRESS': '192.168.56.1'}
# {'IP_ADDRESS': '192.168.56.3'}
# ['192.168.56.1', '192.168.56.4', '192.168.56.3']