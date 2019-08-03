def smallestRange(A, K):
    min_num = min(A)
    max_num = max(A)
    if (max_num - K) <= min_num or (max_num-K) <= (min_num+K):
        return 0
    else:
        return (max_num-K) - (min_num + K)


print(smallestRange([506,4763,8681,4243,4040,8587,9235,442,1865,2820], 5899))
