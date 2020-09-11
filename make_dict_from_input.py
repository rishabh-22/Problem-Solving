n = int(input())
d = {}
for _ in range(n):
    arr = input().split()
    k, *v = arr
    d[k] = " ".join(v)

print(d)
