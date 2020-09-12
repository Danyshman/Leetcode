def maxCoins(piles):
    piles.sort()
    end = len(piles) - 2
    start = 0
    count = 0
    while start < end:
        count += piles[end]
        end -= 2
        start += 1
    return count



print(maxCoins([2,4,1,2,7,8]))
