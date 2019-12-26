def defference(a, b):
    set_a = set(a)
    set_b = set(b)
    comparison = set_a.difference(set_b)
    return list(comparison)


print(defference([1, 2, 3, 4, 5, 6, 7, 8, 999, 9], [1, 2, 4]))
