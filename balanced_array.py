def solve(A):
    count = 0
    left_odd, right_odd, left_even, right_even = [], [], [], []
    le = re = lo = ro = i = 0
    while i < len(A):
        if i % 2 == 0:
            le += A[i]
            re += A[len(A) - i - 1]
            left_even.append(le)
            right_even.append(re)
        else:
            lo += A[i]
            ro += A[len(A) - i - 1]
            left_odd.append(lo)
            right_odd.append(ro)
        i += 1

    for j in range(len(A)):
        if left_odd[j] + right_even[j] == left_even[j] + right_odd[j]:
            count += 1
    return count


arr = [2, 1, 6, 4]
print(solve(arr))
