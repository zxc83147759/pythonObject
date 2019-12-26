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
        pass

    def toDecode(self, str):
        pass

e = Encrypt()
print(e.getcode())
