import copy

grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
ans = copy.copy(grid)

for j in range(1, len(grid[0])):
    ans[0][j] = ans[0][j-1] + grid[0][j]

for j in range(1, len(grid)):
    ans[j][0] = ans[j-1][0] + grid[j][0]

for i in range(1, len(grid)):
    for j in range(1, len(grid[0])):
        ans[i][j] = min(ans[i-1][j], ans[i][j-1]) + grid[i][j]


print(ans[-1][-1])
