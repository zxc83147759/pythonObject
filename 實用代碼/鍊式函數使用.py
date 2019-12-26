def product(a, b):
    return a * b


def add(a, b):
    return a + b


b = True
result = (product if b else add)(5, 6)
print(result)
