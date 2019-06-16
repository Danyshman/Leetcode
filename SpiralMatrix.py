def spiralOrder(matrix):
    height_top = 0
    height_bottom = len(matrix)
    width_right = len(matrix[0])
    width_left = 0
    result_arr = []
    if len(matrix[0]) == 1:
        for arr in matrix:
            result_arr.append(arr[0])
        return result_arr
    while len(result_arr) != (len(matrix[0])*len(matrix)):
        for i in range(width_left, width_right):
            result_arr.append(matrix[height_top][i])
        height_top += 1
        if len(result_arr) == (len(matrix[0])*len(matrix)):
            return result_arr
        for i in range(height_top, height_bottom):
            result_arr.append(matrix[i][width_right-1])
        width_right -= 1
        for i in range(width_right-1, width_left-1, -1):
            result_arr.append(matrix[height_bottom-1][i])
        height_bottom -= 1
        if len(result_arr) == (len(matrix[0])*len(matrix)):
            return result_arr
        for i in range(height_bottom-1, height_top-1, -1):
            result_arr.append(matrix[i][width_left])
        width_left += 1
        if len(result_arr) == (len(matrix[0])*len(matrix)):
            return result_arr

    return result_arr


print(spiralOrder([[2,3,4],
                   [5,6,7],
                   [8,9,10],
                   [11,12,13],
                   [14,15,16]]))
