import re

s = re.search('L', '^Hello', re.I | re.M)
print(s.group())
