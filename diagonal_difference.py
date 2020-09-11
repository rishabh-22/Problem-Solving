#!/bin/python3

import math
import os
import random
import re
import sys
import numpy


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    leading = 0
    # print(arr)
    for i in range(n):
        for j in range(n):
            if i == j:
                leading += arr[i][j]
    print(leading)
    trailing = 0
    for k in range(n):
        for l in range(n):
            if k + l == n-1:
                trailing += arr[k][l]
                print("tr", arr[k][l])
    print(trailing)
    print(abs(trailing-leading))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
