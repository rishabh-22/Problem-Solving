"""
receives a number of strings as inputs, print the number of distinct strings.
"""
import os
from collections import Counter

words = []


def word_order(arr):
    data = Counter(arr)
    total = (set(arr))
    # print(total)
    num = len(total)
    # print(num)
    data_d = dict(data)
    print(data_d)
    final = ''
    for k, v in data_d.items():
        # print(v, end=' ')
        final += str(v) + ' '
    result = '' + str(num)
    result += '\n' + final
    print(result)
    return result


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     t = int(input())
#
#     for t_itr in range(t):
#         t_itr = input()
#         words.append(t_itr)
#
#     result = word_order(words)
#
#     fptr.write(result)
#     fptr.write('\n')
#
#     fptr.close()

word_order(['rishabh', 'bhardwaj', 'rishabh', 'sexy', 'launda', 'bohot', 'sexy', 'rishabh'])
