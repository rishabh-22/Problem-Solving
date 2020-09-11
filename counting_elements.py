def count_occurrences(arr, x):
    res = 0
    for i in range(len(arr)):
        if x == arr[i]:
            res += 1
    return res


def count_elements(arr):
    count = 0
    s = set(arr)
    for i in s:
        if i + 1 in s:
            count += count_occurrences(arr, i)

    print(count)


count_elements([1, 1, 2, 2])
