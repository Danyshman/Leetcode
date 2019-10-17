def largestSumAfterKNegotions(A, K):
    min_index = A.index(min(A))
    for i in range(K):
        A[min_index] = -1*A[min_index]
        min_index = A.index(min(A))
    return sum(A)

print(largestSumAfterKNegotions(A = [2,-3,-1,5,-4], K = 2))