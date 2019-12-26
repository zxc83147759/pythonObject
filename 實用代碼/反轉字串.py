a = 'abcdefghijklmnopqrstuvwxyz'

# 1
print(a[::-1])

# 2
for char in reversed(a):
    print(char,end='')
print()

# 3
num = '123456789'
print(int(str(num)[::-1]))
