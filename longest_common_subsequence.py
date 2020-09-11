def lcs(x, y):
    m, n = len(x), len(y)
    L = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # if i == 0 or j == 0:
            #     L[i][j] = 0
            if x[i - 1] == y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    return L[m][n]


print(lcs('aggtafxb', 'gxtxayb'))
