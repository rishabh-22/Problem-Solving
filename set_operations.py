input()
s = set(map(int, input().split()))
n = int(input())
for i in range(n):
    arr = input().split()
    if len(arr) > 1:
        eval("s.{}({})".format(arr[0], arr[1]))
    else:
        eval("s.{}()".format(arr[0]))

# print(s)
su = 0
for i in s:
	su += i

print(su)