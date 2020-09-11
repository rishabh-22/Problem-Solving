def difference(arr):
    odd_sum = even_sum = 0
    for i, j in enumerate(arr):
        if i % 2 == 0:
            even_sum += j
        else:
            odd_sum += j

    return abs(odd_sum - even_sum)


print(difference([16, 76, 63, 42, 74, 53, 13, 94, 48, 46, 77, 15, 26, 78, 47, 65, 36, 66, 98, 80, 34, 19, 68, 29, 54, 99, 58, 60, 84, 49, 37, 85, 56, 75, 14]))
