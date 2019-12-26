def seq_search(items,key):
    '''順序查找'''
    for index,item in enumerate(items): #計數器，可設定從多少開始
        if item==key:
            return index
    return -1
'''
enumerate:
a=["q","w","e","r"]
#创建一个空字典
b=dict()
#这里i表示的是索引，item表示的是它的值
for i,item in enumerate(a):
    b[i]=item
print(b)

输出：{0: 'q', 1: 'w', 2: 'e', 3: 'r'}
'''