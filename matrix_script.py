import re

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

print(matrix)









# n, m = map(int, input().split())
# a, b = [], ""
# for _ in range(n):
#     a.append(input())
#
# for z in zip(*a):
#     b += "".join(z)
#
# print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", b))
