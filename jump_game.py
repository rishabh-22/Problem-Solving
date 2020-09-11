def can_jump(nums):
    last = len(nums)
    pos = 0

    i = 0
    while i < last:
        if pos < i:
            return False
        pos = max(pos, i + nums[i])
        i += 1

    return True


print(can_jump([3, 2, 1, 0, 4]))
