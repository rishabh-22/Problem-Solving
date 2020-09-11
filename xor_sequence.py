def f(a):
    r = [a, a, 2, 2, a + 2, a + 2, 0, 0]
    return r[a % 8]


def xor_sequence(l, r):
    return f(r) ^ f(l - 1)


print(xor_sequence(5, 9))
