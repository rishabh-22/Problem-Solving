s = set(map(int, input().split()))
n = int(input())
lis = []
for i in range(n):
    x = set(map(int, input().split()))
    lis.append(x)
ans = []
for i in lis:
    if s.issuperset(i) and s != i:
        ans.append(True)
    else:
        ans.append(False)

print(all(ans))
