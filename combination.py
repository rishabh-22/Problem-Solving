"""
find the probability of finding 'a' in combinations of a list.
"""
import os
from itertools import combinations

# m = input()
# arr = list(map(str, input().rstrip().split()))
# n = int(input())
# arr = ['a', 'a', 'c', 'd']
# n = 2
#
#
# def solution(n, arr):
#     le = 0
#     count = 0
#     comb = combinations(arr, n)
#     for i in list(comb):
#         le += 1
#         if 'a' in i:
#             print("yooooo")
#             count += 1
#     # print(count)
#     # print(le)
#     print('%.4f' % (count/le))


# solution(n, arr)


import os
from itertools import combinations


def solution(n, arr):
    le = 0
    count = 0
    comb = combinations(arr, n)
    for i in list(comb):
        le += 1
        if 'a' in i:
            count += 1
    return ('%.4f' % (count / le))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    m = int(input())

    # for t_itr in range(m):
    arr = list(map(str, input().rstrip().split()))

    n = int(input())

    result = solution(n, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
