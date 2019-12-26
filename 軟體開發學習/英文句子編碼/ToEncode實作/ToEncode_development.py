import random
class Encrypt:
    def __init__(self):
        self.setcode()

    def setcode(self):
        a=0
        b=0
        while a% 2==0:
            a = random.randint(0,9)
            b = random.randint(0,9)
        self.code = ''
        c = 'a'
        i = 0
        while i < 26:
            x = c
            y = ord(x) * a + b
            m = y % 26
            self.code += chr(m + 97)
            c = chr(ord(c) + 1)
            i += 1

    def getcode(self):
        return self.code

    # 編碼
    def toEncode(self, str):
        result=''
        for c in str:
            c1=ord(c)>=97
            c2=ord(c)<=122
            if c1 and c2:
                m=ord(c)-97
                result+=self.code[m]
            else:
                result+=c
        return result

    def toDecode(self, str):
        pass

e = Encrypt()
s1='There is no spoon.'
print('Input:',s1)
s2=e.toEncode(s1)
print('Encode:',s2)
print()
