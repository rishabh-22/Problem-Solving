"""
finds the combination of two flavours of ice cream totalling amount
to the exact limit using combinations on a given array.
"""

# from itertools import combinations
# m = 4
# arr = [2, 2, 4, 3]
# arr1 = [1, 4, 5, 3, 2]
# arr2 = [1, 2]
#
#
# def icecreamParlor(m, arr):
#     comb = combinations(arr, 2)
#     for i in list(comb):
#         if sum(i) == m:
#             if i[0] != i[1]:
#                 # print(i)
#                 print(arr.index(i[0])+1)
#                 print(arr.index(i[1])+1)
#             else:
#                 print(arr.index(i[0])+1)
#                 arr.pop(arr.index(i[0]))
#                 print(arr.index(i[1])+2)
#
#
# icecreamParlor(m, arr)


import os
from itertools import combinations

# Complete the icecreamParlor function below.
def icecreamParlor(m, arr):
    comb = combinations(arr, 2)
    for i in list(comb):
        if sum(i) == m:
            if i[0] != i[1]:
                first = arr.index(i[0])+1
                second = arr.index(i[1])+1
                return first, second
            else:
                first = arr.index(i[0])+1
                arr.pop(arr.index(i[0]))
                second = arr.index(i[1])+2
                return first, second


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
