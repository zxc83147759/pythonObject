from collections import Counter

str1 = 'abbbc' #1a 3b 1c
str2 = 'babcb' #1a 3b 1c
str3 = 'aabbc' #2a 2b 1c
print(Counter(str1) == Counter(str2))
print(Counter(str1) == Counter(str3))
