"""
to sort a spreadsheet input based on a specific index.
"""

import math
import os
import random
import re
import sys
import operator


def athlete_sort(arr, k):
    arr.sort(key=operator.itemgetter(k))
    for ath in arr:
        print(*ath, sep=" ")


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    athlete_sort(arr, k)
