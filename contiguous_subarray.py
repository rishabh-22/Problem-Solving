nums = [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, ]

num = {0: 0}
s = 0
ans = 0
for i in range(len(nums)):
    s += (1 if i == 1 else -1)
    if s in num:
        ans = max(ans, i + 1 - num[s])
    else:
        num[s] = i+1

print(ans)
