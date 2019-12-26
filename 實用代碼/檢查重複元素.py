def all_unique(list1):
    return len(list1) == len(set(list1))


x = [1, 2, 2, 2, 3, 4, 5, 6, 7, 7, 8]
y = [1, 2, 3, 4, 5]
print(all_unique(x))
print(all_unique(y))
