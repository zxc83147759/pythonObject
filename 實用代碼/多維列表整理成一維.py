def spread(list1):
    ret=[]
    for i in list1:
        if isinstance(i,list): #判斷是否為同一個type
            ret.extend(i)
        else:
            ret.append(i)
    return ret
x=[[1,2,3],4,5,6,[7,8,9],2,3,4]
print(spread(x))
