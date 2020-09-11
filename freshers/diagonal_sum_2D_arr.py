array = [[5, 12, 17], [13, 4, 8], [9, 21, 14]]


def sum_of_diagonal(arr):
    su = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i + j == len(arr)-1:
            # if i == j:
                su += arr[i][j]
    return su


print(sum_of_diagonal(array))
