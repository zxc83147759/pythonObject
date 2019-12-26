import re
'''
re.sub(pattern,repl,string,count=0)
pattern符合後將string用repl替換掉 count是最多替換幾次 預設最大數量
'''
s='playing 4 hour a day'
obj =re.sub(r'^.*$','Working',s)
print(obj)