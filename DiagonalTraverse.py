def findDiagonalOrder(matrix):
    if matrix == [[]] or not matrix:
        return []
    len_rows = len(matrix)
    len_cols = len(matrix[0])
    pos = [0,0]
    result = []
    dir = 'up'
    while True:
        result.append(matrix[pos[0]][pos[1]])
        if pos == [len_rows-1, len_cols-1]:
            return result
        elif dir=='up' and pos[1]+1>=len_cols:
            pos[0] += 1
            dir = 'down'
        elif dir == 'up' and pos[0]-1<0:
            pos[1] += 1
            dir = 'down'
        elif dir=='down' and pos[0]+1 >=len_rows:
            pos[1] += 1
            dir='up'
        elif dir=='down' and pos[1]-1<0:
            pos[0] += 1
            dir= 'up'
        elif dir=='down':
            pos[0] += 1
            pos[1] -= 1
        elif dir =='up':
            pos[1] += 1
            pos[0] -= 1


print(findDiagonalOrder([
]))