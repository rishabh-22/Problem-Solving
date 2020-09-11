N = int(input())
l = []
for i in range(N):
    arr = input().split()
    if len(arr) == 2:
        eval("l.{}({})".format(arr[0], arr[1]))
    elif len(arr) == 3:
        eval("l.{}({}, {})".format(arr[0], arr[1], arr[2]))
    elif len(arr) == 1 and arr[0] != "print":
        eval("l.{}()".format(arr[0]))
    else:
        print(l)
