def generate(numRows):
    if numRows == 0:
        return []
    elif numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1], [1,1]]
    trianlge = [[1], [1,1]]
    for i in range(numRows-2):
        new_base = [1]
        for j in range(1,len(trianlge[-1])):
            new_base.append(trianlge[-1][j-1]+trianlge[-1][j])
        new_base.append(1)
        trianlge.append(new_base)
    return trianlge

print(generate(5))

