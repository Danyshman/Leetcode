def searchMatrix(matrix, target):
    if not matrix:
        return False
    elif len(matrix) == 1:
        return binary_search(matrix[0], target)
    else:
        for i in range(len(matrix)-1):
            if matrix[i+1][0] > target >= matrix[i][0]:
                return binary_search(matrix[i], target)
    return binary_search(matrix[-1], target)


def binary_search(arr, target):
    if not arr:
        return False
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            right = mid-1
        elif target > arr[mid]:
            left = mid + 1
    return False


print(searchMatrix([], 0))