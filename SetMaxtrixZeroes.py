def setZeroes(matrix):
    zero_indexes_rows = set()
    zero_indexes_col = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                zero_indexes_rows.add(i)
                zero_indexes_col.add(j)
    for i in zero_indexes_rows:
        matrix[i] = [0 for i in range(len(matrix[i]))]
    for j in zero_indexes_col:
        for arr in matrix:
            arr[j] = 0
    return matrix



print(setZeroes([
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]))