# cartesian product of 2 arrays inputted by the user.


def cartesian(lis1, lis2):
    final = []
    for item1 in lis1:
        for item2 in lis2:
            final.append((item1,  item2))
    # print(" ".join(str(x) for x in final))
    print(*final)


lis1 = input("Enter first list:\n")
lis1 = list(lis1.split(" "))
lis1 = [int(i) for i in lis1]
lis2 = input("Enter second list:\n")
lis2 = list(lis2.split(" "))
lis2 = [int(i) for i in lis2]
# arr = list(map(int, input().rstrip().split()))  # how to get array as in input.
cartesian(lis1, lis2)
# cartesian([1, 2], [3, 4])
