from typing import Tuple, List


def mark_neighbours(matrix: List, pos: Tuple):
    r, c = pos

    if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]) or matrix[r][c] != 1:
        return

    matrix[r][c] = 0

    mark_neighbours(matrix, (r + 1, c))
    mark_neighbours(matrix, (r - 1, c))
    mark_neighbours(matrix, (r, c + 1))
    mark_neighbours(matrix, (r, c - 1))


def count_islands(grid):
    grid = [[int(j) for j in x] for x in grid]
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                mark_neighbours(grid, (i, j))
                count += 1
                # print(i, j)

    return count


grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
print(count_islands(grid))
