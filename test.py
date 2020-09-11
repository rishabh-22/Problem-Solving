import sys


def perfectPeak(A):
    if len(A) == 1:
        return 1
    for i in range(1, len(A)):
        if i != len(A)-1:
            if max(A[:i]) < A[i] < min(A[i + 1:]):
                return 1
        elif A[len(A)-1] == max(A):
            return 1
    return 0

    # abs_maxi = A[0]
    # so_far_maxi = A[0]
    # ans = 0
    # n = len(A)
    # for i in range(1, n):
    #     if A[i] > so_far_maxi:
    #         so_far_maxi = A[i]
    #     if A[i] > abs_maxi:
    #         if ans == 0:
    #             abs_maxi = so_far_maxi
    #         ans = 1
    #     if A[i] < abs_maxi:
    #         ans = 0
    #         abs_maxi = so_far_maxi
    # if abs_maxi == A[n - 1]:
    #     return 0
    # return ans


arr = [9488, 25784, 5652, 9861, 31311, 8611, 1671, 7129, 28183, 2743, 11059, 4473, 7927, 21287, 2259, 7214, 32529]
arr1 = [9895, 30334, 17674, 23812, 20038, 25668, 6869, 1870, 4665, 27645, 7712, 17036, 31323, 8724, 28254, 28704, 26300, 25548, 15142, 12860, 19913, 32663, 32758]

print(perfectPeak(arr1))
