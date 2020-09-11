nums = [5, 8, 19, 10, 20, 3, 7]
k = 7


def sub_array_sum_k(arr, k):
    curr, left, right = 0, 0, 0
    while right < len(arr):
        curr = sum(arr[left:right+1])
        if curr == k:
            return 1
        elif curr < k:
            right += 1
        elif curr > k:
            left += 1
    return 0


print(sub_array_sum_k(nums, k))

