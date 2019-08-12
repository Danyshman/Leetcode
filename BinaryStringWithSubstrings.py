def queryString(S, N):
    for i in range(1, N+1):
        if bin(i)[2:] not in S:
            return False
    return True

print(queryString(S = "0110", N = 4))