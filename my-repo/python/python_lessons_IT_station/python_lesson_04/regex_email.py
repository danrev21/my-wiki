#!/usr/bin/env python

import re

# Matching email addresses
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
text = "Contact support@example.com for assistance or visit www.example.com."
emails = re.findall(email_pattern, text)
print(emails)  # Output: ['support@example.com']