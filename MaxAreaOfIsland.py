def maxAreaOfIsland(grid):
    max_area = 0
    global_checked_points = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1 and (i,j) not in global_checked_points:
                checked_points = []
                should_check = [(i,j)]
                area = 1
                while len(should_check) != 0:
                    for point in should_check:
                        global_checked_points.append(point)
                        if point[1] != 0:
                            if grid[point[0]][point[1] - 1] == 1 and (point[0], point[1] - 1) not in checked_points and (point[0], point[1] - 1) not in should_check:
                                should_check.append((point[0], point[1] - 1))
                                area += 1
                        if point[0] != 0:
                            if grid[point[0] - 1][point[1]] == 1 and (point[0] - 1, point[1]) not in checked_points and (point[0] - 1, point[1]) not in should_check:
                                should_check.append((point[0] - 1, point[1]))
                                area += 1
                        if point[1] != len(grid[point[0]]) - 1:
                            if grid[point[0]][point[1] + 1] == 1 and (point[0], point[1] + 1) not in checked_points and (point[0], point[1] + 1) not in should_check:
                                should_check.append((point[0], point[1] + 1))
                                area += 1
                        if point[0] != len(grid) - 1:
                            if grid[point[0] + 1][point[1]] == 1 and (point[0] + 1, point[1]) not in checked_points and (point[0] + 1, point[1]) not in should_check:
                                should_check.append((point[0] + 1, point[1]))
                                area += 1
                        checked_points.append((point[0], point[1]))
                        should_check.remove((point[0], point[1]))
                if area > max_area:
                    max_area = area

    return max_area


print(maxAreaOfIsland([[1,1,1],
                       [0,1,1]]))

