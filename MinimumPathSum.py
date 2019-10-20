def minPathSum(grid):
    r_len = len(grid)
    c_len = len(grid[0])
    if r_len == 0 or c_len == 0 or grid is None:
        return 0
    for i in range(1, r_len):
        grid[i][0] = grid[i-1][0] + grid[i][0]
    for i in range(1, c_len):
        grid[0][i] = grid[0][i] + grid[0][i-1]
    for i in range(1, r_len):
        for j in range(1, c_len):
            grid[i][j] = min(grid[i][j]+grid[i-1][j],grid[i][j]+grid[i][j-1])
    return grid[r_len-1][c_len-1]


print(minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))