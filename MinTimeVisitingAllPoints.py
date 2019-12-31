def minTimeToVisitAllPoints(points):
    total_sec = 0
    if len(points) == 1:
        return 0
    else:
        for i in range(len(points)-1):
            start = points[i]
            end = points[i+1]
            total_sec += max(abs(start[0]-end[0]), abs(start[1]-end[1]))
        return total_sec


print(minTimeToVisitAllPoints([[3,2],[-2,2]]))

