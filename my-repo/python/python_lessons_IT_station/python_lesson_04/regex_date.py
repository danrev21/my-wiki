#!/usr/bin/env python

import re

# Extracting dates in MM/DD/YYYY format
date_pattern = r'\b\d{1,2}/\d{1,2}/\d{4}\b'
text = "Meeting on 05/20/2023 is rescheduled to 06/10/2023."
dates = re.findall(date_pattern, text)
print(dates)   # Output: ['05/20/2023', '06/10/2023']