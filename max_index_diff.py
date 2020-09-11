# to find the max difference between two indices(i,j) provided arr[i]<arr[j]

def maxIndexDiff(arr, n):
    last = n - 1
    first = 0
    max_diff = 0
    while first < last:
        if arr[first] < arr[last]:
            max_diff = max(max_diff, last - first)
        # else:
        first += 1
        last -= 1
    return max_diff


print(maxIndexDiff([65, 6, 74, 94, 56, 89, 9, 63, 75, 25, 34, 68, 93, 48, 16], 15))
