def maxIncreaseKeepingSkyline(grid):
    row_maxs = [0 for __ in range(len(grid))]
    col_max = [0 for __ in range(len(grid[0]))]
    for i in range(len(grid)):
        row_maxs[i] = max(grid[i])
    for i in range(len(grid[0])):
        for j in grid:
            if j[i] > col_max[i]:
                col_max[i] = j[i]
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            count += min(row_maxs[i], col_max[j]) - grid[i][j]
    return count


print(maxIncreaseKeepingSkyline([
  [3, 0, 8, 4],
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ]))

