from math import ceil


def chunk(list1, size):
    return list(map(lambda x: list1[x * size:x * size + size], list(range(0, ceil(len(list1) / size)))))

print(chunk([1,2,3,4,5],2))
