from sys import maxsize
"""
Find the minimum sub array Al, Al+1 ,…, Ar so if we sort(in ascending order) that sub array, then the whole array should get sorted.
If A is already sorted, output -1.

eg:
Input 1:
A = [1, 3, 2, 4, 5]
Return: [1, 2]

Input 2:
A = [1, 2, 3, 4, 5]
Return: [-1]
"""


def sub_unsort(arr):
    flag = False
    n = len(arr) - 1
    p1 = n
    p2 = 0
    maxx = arr[0]
    minn = maxsize
    for i in range(n):
        if arr[i] > arr[i + 1] or arr[i + 1] < maxx:
            flag = True
            maxx = max(maxx, arr[i], arr[i + 1])
            minn = min(minn, arr[i], arr[i + 1])
            p1 = min(p1, i)
            p2 = max(p2, i + 1)

    j = p1
    while j >= 0:
        if arr[j] > minn:
            p1 = min(p1, j)
        j -= 1

    if flag:
        return p1, p2
    else:
        return [-1]


print(sub_unsort([1, 3, 2, 4, 5]))
