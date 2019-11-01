def maxCount(m,n, ops):
    row = 400001
    col = 400001
    for op in ops:
        if op[0] < row:
            row = op[0]
        if op[1] < col:
            col = op[1]
    return row*col


print(maxCount(m = 3, n = 3, ops = [[2,2],[3,3]]))
