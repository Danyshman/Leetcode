def arrangeCoins(n):
    if n == 0:
        return 1
    len_stairs = 1
    count = 0
    while n >= len_stairs:
        count += 1
        n -= len_stairs
        len_stairs += 1
    return count


print(arrangeCoins(1))