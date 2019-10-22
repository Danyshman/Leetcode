def numberOfArithmeticSlices(A):
    dp = [0 for __ in range(len(A))]
    count = 0
    if len(A) < 3:
        return 0
    else:
        if A[2]-A[1] == A[1]-A[0]:
            dp[2] = 1
            count += 1
    for i in range(3,len(A)):
        if dp[i-1] > 0 and A[i]-A[i-1] == A[i-1]-A[i-2]:
            dp[i] += dp[i-1] + 1
            count += dp[i]
        elif dp[i-1] == 0 and A[i]-A[i-1] == A[i-1]-A[i-2]:
            dp[i] += 1
            count += 1
    return count


print(numberOfArithmeticSlices([1, 2, 3, 4,5,7,8,9]))