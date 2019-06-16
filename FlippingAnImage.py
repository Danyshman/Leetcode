def flipAndInvertImage(A):
    for i in range(len(A)):
        A[i] = A[i][::-1]
    for arr in A:
        for i in range(len(arr)):
            if arr[i] == 0:
                arr[i] = 1
            else:
                arr[i] = 0
    return A


print(flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))