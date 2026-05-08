#!/usr/bin/env python

import re;

line = '192.168.56.4 - - [14/Nov/2023:03:11:42 +0000] "GET / HTTP/1.1" 200 10926 "-" "curl/7.81.0"';

# we will parse the line using next regular expressions:
#   ip_regex = r'(?P<IP_ADDRESS>\d+\.\d+\.\d+\.\d+)'
#   status_regex = r'(?P<STATUS>\s\d{3}\s)'
#   time_regex = r'\[(?P<Time>.*) \+\d{4}\]'
#   request_regex = r' "(?P<REQUEST>[A-Z]+).*" \d{3}'
#   bytes_regex = r'\d{3} (?P<bytes_sent>\d+) "'

print(f"Parsing this line: \n{line}\n--------------")

ip_regex = r'(?P<IP_ADDRESS>\d+\.\d+\.\d+\.\d+)'; 
ip_out = re.match(ip_regex, line); # we can use re.search() here and get the same result
print(ip_out.groupdict())                 # output: {'IP_ADDRESS': '192.168.56.4'}

status_regex = r' (?P<status>\d{3}) \d+';
status_out = re.search(status_regex, line);
print(status_out.groupdict())             # output: {'STATUS': '200'}

time_regex = r'\[(?P<TIME>.*) \+\d{4}\]';
time_out = re.search(time_regex, line);
print(time_out.groupdict())               # output: {'Time': '14/Nov/2023:03:11:42'}

request_regex = r' "(?P<REQUEST>[A-Z]+).*" \d{3}';
request_out = re.search(request_regex, line);
print(request_out.groupdict())            # output: {'REQUEST': 'GET'}

bytes_regex = r'\d{3} (?P<bytes_sent>\d+) "';
bytes_out = re.search(bytes_regex, line);
print(bytes_out.groupdict())              # output: {'bytes_sent': '10926'}

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
                              "-"\s+# "-" + whitespace
                              "(?P<agent>.*)"
                              ''', re.VERBOSE);
# line_regex = re.compile(r'(?P<remote_host>\S+)\s+\S+\s+\S+\s+\[(?P<Time>.+)\s+\+\d*\]\s+"[^"]+"\s+(?P<status>\d+)\s+(?P<bytes_sent>-|\d+)\s*"-"\s+"(?P<agent>.*)"')
line_out = line_regex.match(line);    # with re.search() the same 
print(line_out.groupdict())  
# output: {'remote_host': '192.168.56.4', 'Time': '14/Nov/2023:03:11:42', 'status': '200', 'bytes_sent': '10926', 'agent': 'curl/7.81.0'}


