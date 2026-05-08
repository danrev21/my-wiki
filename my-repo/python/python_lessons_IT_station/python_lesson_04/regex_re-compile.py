#!/usr/bin/env python

# The re.compile() method allows you to precompile a 
# regular expression pattern, improving performance 
# if the pattern is used multiple times.

import re

pattern = re.compile(r'\b\d{1,2}/\d{1,2}/\d{4}\b')
text = "Meeting on 05/20/2023 is rescheduled to 06/10/2023."
dates = pattern.findall(text)
print(dates)   # Output: ['05/20/2023', '06/10/2023']