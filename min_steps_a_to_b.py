def cover_points(A, B):
    count = 0
    for i in range(len(B)-1):
        start = [A[i], B[i]]
        # end = [A[i+1], B[i+1]]
        x = abs(A[0] - B[0])
        y = abs(A[i] - B[i])

        while x > 0 or y > 0:
            if x > 0:
                start[0] += 1
                x -= 1
            if y > 0:
                start[1] += 1
                y -= 1
            count += 1

    return count


print(cover_points([4, 8, -7, -5, -13, 9, -7, 8], [4, -15, -10, -3, -13, 12, 8, -8]))


# def coverPoints(self, A, B):
#     count = 0
#     for i in range(1, len(A)):
#         count += max(abs(A[i] - A[i - 1]), abs(B[i] - B[i - 1]))
#     return count
