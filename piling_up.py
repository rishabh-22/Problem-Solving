def piling_up(arr):
    flag = True
    print("inside", len(arr))
    base_idx = 0 if arr[0] >= arr[-1] else -1
    base = arr.pop(base_idx)
    while len(arr) > 0:
        if arr[0] >= arr[-1]:
            nex = arr.pop(0)
        else:
            nex = arr.pop(-1)
        if nex <= base:
            pass
        else:
            flag = False

    if flag:
        return "Yes"
    else:
        return "No"


# n = int(input())
# for i in range(n):
#     input()
#     arr = list(map(int, input().split()))
#     print("arr len: ", len(arr))
#     print(piling_up(arr))


with open("test1") as file:
    lines = file.readlines()
    n = lines.pop(0)
    for i in range(len(lines)):
        if i % 2:
            lis = list(map(int, lines[i].split()))
            print("outside: ", len(lis))
            print(piling_up(lis))


# lis = list(map(int, li.split()))
# print(len(lis))
# print(piling_up(lis))