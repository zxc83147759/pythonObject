def compact(list1):
    return list(filter(bool,list1))
print(compact([0,1,False,2,'',3,'a','s',34]))