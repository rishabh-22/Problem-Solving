def drive_partition(arr):
    arr.sort(reverse=True)
    one = []
    two = []
    one.append(arr[0])
    arr.pop(0)
    two.append(arr[0])
    arr.pop(0)
    for i in arr:
        if sum(one) < sum(two):
            one.append(i)
        else:
            two.append(i)
    print(one, "\n", two)
    print(abs(sum(one) - sum(two)))


drive_partition([10, 11, 10, 10])
