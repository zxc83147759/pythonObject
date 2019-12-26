def merge_two_dicts(a, b):
    c = a.copy()
    c.update(b)
    return c


a = {'x': 1, 'y': 2}
b = {'y': 3, 'z': 4}
print({**a, **b})
print(dict(a.items() | b.items()))
print(merge_two_dicts(a, b))
