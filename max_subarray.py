def max_sub_array(nums):
    max_so_far = 0
    max_ending_here = 0
    start, end, s = 0, 0, 0
    for i in range(len(nums)):
        max_ending_here += nums[i]
        if max_ending_here < 0:
            max_ending_here = 0
            s = i+1
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            end = i
            start = s

    return max_so_far, (start, end)


print(max_sub_array([4, -3, -2, 2, 3, 1, -2, -3, 4, 2, -6, -3, -1, 3, 1, 2]))


def maxSubArray(A):
    max_so_far = 0
    max_ending_here = 0
    for i in range(len(A)):
        max_ending_here += A[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


print(maxSubArray([4, -3, -2, 2, 3, 1, -2, -3, 4, 2, -6, -3, -1, 3, 1, 2]))
