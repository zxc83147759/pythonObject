from collections import Counter
def anagram(first_str,second_str):
    return Counter(first_str)==Counter(second_str)
print(Counter('3acbd'))
print(Counter('abcd3'))
print(anagram('abcd3','3acbd'))