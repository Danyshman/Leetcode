def isToeplitzMatrix(matrix):
    for i in range(len(matrix)-1):
        for j in range(len(matrix[i])-1):
            if matrix[i][j] != matrix[i+1][j+1]:
                return False
    return True


print(isToeplitzMatrix([
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]))