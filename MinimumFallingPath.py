def minFallingPathSum(A):
    for i in range(1, len(A)):
        for j in range(len(A[0])):
            if j == 0:
                A[i][j] = min(A[i-1][j], A[i-1][j+1]) + A[i][j]
            elif j == len(A[0])-1:
                A[i][j] = min(A[i-1][j], A[i-1][j-1]) + A[i][j]
            else:
                A[i][j] = A[i][j] + min(A[i-1][j], A[i-1][j-1], A[i-1][j+1])
    return min(A[-1])


print(minFallingPathSum([[1,2],[2,2]]))