from collections import defaultdict

d = defaultdict(list)
n, m = map(int, input().split())
arr = []
data = []
for i in range(n):
    arr.append(input())

for j in range(m):
    data.append(input())

# print(arr)
# print(data)
for i, element in enumerate(arr):
    l = []
    for j in data:
        if j == element:
            d[j].append(i+1)
        else:
            l.append(-1)
            d[j].append(-1)
            break

for i in data:
    if i in d:
        print(*d[i])
    else:
        print(-1)


# from collections import defaultdict
# d = defaultdict(list)
# list1 = []
#
# n, m = map(int, input().split())
#
# for i in range(n):
#     d[input()].append(i+1)
#
# for i in range(m):
#     list1 = list1+[input()]
#
# for i in list1:
#     if i in d:
#         # print(" ".join(map(str, d[i])))
#         print(*d[i])
#     else:
#         print(-1)
