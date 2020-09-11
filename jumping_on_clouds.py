def jumping_on_clouds(c, k):
    e = 100
    counter = 0
    # for i in range(k, len(c), k):
    i = k
    if c[i % len(c)] == 1:
        e -= 2
    while i != 0:
        if c[(i+k) % len(c)] == 1:
            e -= 2
        counter += 1
        i = (i+k) % len(c)
    return e - counter - 1


print(jumping_on_clouds([1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1], 19))
