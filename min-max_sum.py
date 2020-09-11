"""
finds the min and max sum for 4 out of 5 elements in a list.
"""

from itertools import permutations

arr = list(map(int, input().rstrip().split()))


def min_max_sum(arr):
    perm = permutations(arr, 4)
    lis = list(perm)
    result = []
    for element in lis:
        result.append(sum(element))
    print(max(result))
    print(min(result))


min_max_sum(arr)
