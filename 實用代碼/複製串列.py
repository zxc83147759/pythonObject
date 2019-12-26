# both a and b will be[10,2,3,4,5]
a = [1, 2, 3, 4, 5]
b = a
b[0] = 10
# only b will change to [10,2,3,4,5]
a = [1, 2, 3, 4, 5]
b = a[:]
b[0] = 10
# copy list
a = [1, 2, 3, 4, 5]
print(list(a))
# use copy
print(a.copy())
# copy nested lists using copy.deepcopy
from copy import deepcopy

l = [[1, 2], [3, 4]]
l2 = deepcopy(l)
print(l2)
