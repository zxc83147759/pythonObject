dict1={'test':1,'test1':2,'test3':3,'test4':4}
print(dict1)
print(min(dict1,key=dict1.get))
print(max(dict1,key=dict1.get))