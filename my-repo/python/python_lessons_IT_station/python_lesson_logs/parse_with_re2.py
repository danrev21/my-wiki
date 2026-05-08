#!/usr/bin/env python

# выводит уникальные ip из логов
# to run script: ./parse_with_re2.py ./apache_logs/access.log


import re
import sys

ip_regex = r'(?P<IP_ADDRESS>\d+\.\d+\.\d+\.\d+)'

log_file = sys.argv[1]
ip_addresses = []
with open(log_file) as file:
    for line in file.readlines():
        ip_out = re.match(ip_regex, line)
        print(ip_out.groupdict()) 
        ip_address = ip_out["IP_ADDRESS"]
        if ip_address not in ip_addresses:
            ip_addresses.append(ip_address)
print(ip_addresses)

# output: 
# ....
# {'IP_ADDRESS': '192.168.56.1'}
# {'IP_ADDRESS': '192.168.56.1'}
# {'IP_ADDRESS': '192.168.56.3'}
# ['192.168.56.1', '192.168.56.4', '192.168.56.3']