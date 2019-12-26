import re

'''
re.match(pattern,string,flages)
pattern 正規表達式模式
string 指定字串
flags  更改正規表達式的行為
成功返回字串 失敗返回none

match(r'XXX')
有r的話:
re.compile(r'item\n')
沒r的話:
re.compile('item\\n')
r=原字符串
'''
strTest = 'Hello Python Programming'
mobj = re.match(r'hello', strTest, re.I)  #字串與匹配模式比較 re.I是忽略大小寫 最終結果給mobj
print(mobj.group())
