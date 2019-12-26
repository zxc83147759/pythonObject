import re
def check(str):
    s=re.compile(r'[^A-Z]')
    str=s.search(str)
    return not bool(str)
print(check('HELLOWPYTHON'))
print(check('hellopython'))