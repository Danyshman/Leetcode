def minOperations(n):
    count = 0
    if n % 2 == 1:
        for i in range(n, n*2, 2):
            count += i-n
    else:
        for i in range(n+1, n*2, 2):
            count += i-n
    return count


print(minOperations(6))