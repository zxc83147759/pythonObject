import itertools

list1=[i for i in itertools.permutations('ABCD')]
print(list1)
list2=[i for i in itertools.combinations('ABCD',3)]
print(list2)
list3=[i for i in itertools.product('ABCD','123')]
print(list3)
