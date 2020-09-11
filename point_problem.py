# to find the number of points based on the elements present in list. if element in array in A set, +1, if in B, -1.

# arr = list(map(int, input().rstrip().split()))  # how to take array as in i/p
array = input("Enter the array:\n")
array = list(array.split(" "))
array = [int(i) for i in array]
set_A = input("Enter first set:\n")
set_A = set(set_A.split(" "))
set_A = {int(i) for i in set_A}
set_B = input("Enter second set:\n")
set_B = set(set_B.split(" "))
set_B = {int(i) for i in set_B}

points = 0
for element in array:
    if element in set_A:
        points += 1
    elif element in set_B:
        points -= 1
    else:
        pass

print(points)

