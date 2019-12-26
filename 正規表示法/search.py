import re

'''
re.match(pattern,string,flages)
pattern 正規表達式模式
string 指定字串
flags  更改正規表達式的行為
成功返回字串 失敗返回none
'''
str1 = 'Hello python programming'
sobj = re.search(r'programming', str1, re.I)
print(sobj.group())

'''
在開頭搜尋
sobj = re.search(r"^programming", str1, re.I)
在尾巴搜尋
sobj = re.search(r'programming$', str1, re.I)
'''


