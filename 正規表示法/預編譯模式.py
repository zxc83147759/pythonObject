import re
'''
compile 可先設定模式
'''
compat =re.compile(r'(\d)') #\d=取第一個數字
sboj=compat.search('Lalalasdlsd 123')
print(sboj.group())
mobj=compat.match('234 123123asdfasdesdsad')
print(mobj.group())
