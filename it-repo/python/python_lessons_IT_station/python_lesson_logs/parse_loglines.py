#!/usr/bin/env python

'''
we have log file:
192.168.56.1 - - [14/Nov/2023:03:11:42 +0000] "POST / HTTP/1.1" 200 3460 "-" "python-requests/2.31.0"
192.168.56.3 - - [14/Nov/2023:03:11:42 +0000] "GET / HTTP/1.1" 200 3460 "-" "python-requests/2.31.0"
192.168.56.4 - - [14/Nov/2023:03:11:42 +0000] "GET / HTTP/1.1" 200 10926 "-" "curl/7.81.0"
'''

# to run script: ./parse_loglines.py ./apache_logs/access.log

import sys
def split_line(line):
    splitted_line = line.split()
    return {
        "ip_address": splitted_line[0],
        "bytes_sent": splitted_line[9],
        "agent_data": " ".join(splitted_line[11:])
    }

if __name__ ==  "__main__":
    log_file = sys.argv[1]
    with open(log_file) as file:
        line_num = 1
        for line in file.readlines():
            splitted_line = split_line(line)
            print(f"line {line_num}:     {splitted_line}")
            line_num += 1

# Output:
# line 55:     {'ip_address': '192.168.56.1', 'bytes_sent': '3460', 'agent_data': '"python-requests/2.31.0"'}
# line 56:     {'ip_address': '192.168.56.3', 'bytes_sent': '3460', 'agent_data': '"python-requests/2.31.0"'}
# line 57:     {'ip_address': '192.168.56.4', 'bytes_sent': '10926', 'agent_data': '"curl/7.81.0"'}  
   
    ip_addresses = []
    with open(log_file) as file:
        for line in file.readlines():
            splitted_line = split_line(line)
            ip_address = splitted_line["ip_address"]
            if ip_address not in ip_addresses:
                ip_addresses.append(ip_address)
    print(f"Uniq IPs: {ip_addresses}")

# Output:
# Uniq IPs: ['192.168.56.1', '192.168.56.4', '192.168.56.3']
