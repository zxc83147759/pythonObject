def most_frquent(list1):
    return max(set(list1),key=list1.count)

list1=[1,2,1,2,3,1,2,3,1,2,2,2]
print(most_frquent(list1))
