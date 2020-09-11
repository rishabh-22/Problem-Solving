# x = []
# def new():
#     while True:
#         z = input()
#         if z == "" or z == "\n":
#             break
#         else:
#             x.append(z)
# new()
# print(x)

from itertools import groupby
s = "1222311"

# lis = [(len(list(c)), int(k)) for k, c in groupby(s)]

g = groupby(s)
for i, j in g:
    print(len(list(j)), i)
