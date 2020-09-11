from collections import defaultdict

d1 = defaultdict(int)
n = int(input())
a = list(map(int, input().split()))
for x, y in enumerate(a, 1):
    d1[x] = y
d2 = {v: k for k, v in d1.items()}
for x, y in sorted(d1.items(), key=lambda k_v: k_v[1]):
    print(d2[x])
