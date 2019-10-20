def uniquePathWithObstacles(obstacleGrid):
    r_len = len(obstacleGrid)
    c_len = len(obstacleGrid[0])
    if r_len == 0 or c_len == 0 or obstacleGrid is None:
        return 0
    empty_grid = [[0 for j in range(c_len)] for i in range(r_len)]
    for i in range(r_len):
        if obstacleGrid[i][0] != 1:
            empty_grid[i][0] = 1
        else:
            break
    for i in range(c_len):
        if obstacleGrid[0][i] != 1:
            empty_grid[0][i] = 1
        else:
            break
    for i in range(1,r_len):
        for j in range(1,c_len):
            if obstacleGrid[i][j] != 1:
                empty_grid[i][j] += empty_grid[i-1][j] + empty_grid[i][j-1]
    return empty_grid[r_len-1][c_len-1]


print(uniquePathWithObstacles([
  [0,0,0,0],
  [0,0,1,0],
  [0,0,0,0],
  [1,0,0,0]
]))
