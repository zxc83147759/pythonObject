from random import shuffle

# 定義Encrypt類別
class Encrypt:
    # 建立Encrypt物件同事建立密碼表
    def __init__(self, str=None):
        # 設定CODE
        if str == None:
            self.code = [chr(i) for i in range(97, 123)]
            shuffle(self.code)
        else:
            self.code = list(str)
        # 設定Alph
        self.alph = [chr(i) for i in range(97, 123)]

    def __str__(self):
        code = ''.join(self.code)
        return 'code:' + code

    # 編碼
    def toEncode(self, str):
        # 暫存編碼結果的字串
        result = ''
        for i in str:
            # 判斷該字源是否為英文小寫字母
            # 若是英文小寫字母就進行編碼
            if i in self.code:
                j = self.alph.index(i)
                result += self.code[j]
            else:
                result += i
        return result

    # 解碼
    def toDecode(self, str):
        # 暫存
        result = ''
        # 用迴圈跑字元
        for i in str:
            # 判斷該字元是否為英文小寫字母
            # 若是英文小寫字母就
            # 進行解碼
            if i in self.code:
                j = self.code.index(i)
                result += self.alph[j]
            else:
                result += i
        # 結束回傳解碼過的字串
        return result


if __name__ == '__main__':
    e = Encrypt()
    print()
    print(e)
    s1 = 'There is no spoon.'
    print('Input:', s1)
    s2 = e.toEncode(s1)
    print('Encode:', s2)
    s3 = e.toDecode(s2)
    print('Decode:', s3)
    print()
