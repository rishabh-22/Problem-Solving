def find_triplets(arr, n):
    found = False
    for i in range(n - 1):

        # Find all pairs with sum
        # equals to "-arr[i]"
        s = set()
        for j in range(i + 1, n):
            x = -(arr[i] + arr[j])
            if x in s:
                print(x, arr[i], arr[j])
                found = True
            else:
                s.add(arr[j])
    if not found:
        print("No Triplet Found")


def findTriplets(arr, n):
    found = False

    # sort array elements
    arr.sort()

    for i in range(0, n - 1):

        # initialize left and right
        l = i + 1
        r = n - 1
        x = arr[i]
        while l < r:

            if x + arr[l] + arr[r] == 0:
                # print elements if it's sum is zero
                print(x, arr[l], arr[r])
                l += 1
                r -= 1
                found = True

            # If sum of three elements is less
            # than zero then increment in left
            elif x + arr[l] + arr[r] < 0:
                l += 1

            # if sum is greater than zero than
            # decrement in right side
            else:
                r -= 1

    if not found:
        print(" No Triplet Found")


arr = [-1, 1, 2, -2, 0, 4, -3]
findTriplets(arr, len(arr))
find_triplets(arr, len(arr))
