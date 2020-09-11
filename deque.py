from collections import deque
d = deque()
for i in range(int(input())):
    arr = input().split()
    if len(arr) > 1:
        eval("d.{}({})".format(arr[0], arr[1]))
    else:
        eval("d.{}()".format(arr[0]))

for i in d:
    print(i, end=" ")
