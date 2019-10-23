def merge(intervals):
    intervals.sort()
    i = 0
    while i < len(intervals)-1:
        if intervals[i + 1][0] <= intervals[i][1]:
            intervals[i: i + 2] = [[min(intervals[i][0], intervals[i+1][0]), max(intervals[i + 1][1], intervals[i][1])]]
        else:
            i += 1
    return intervals


print(merge([[1,4],[2,3]]))