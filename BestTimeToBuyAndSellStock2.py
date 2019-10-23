def maxProfit(prices):
    # dp = [[0 for __ in range(len(prices))] for __ in range(len(prices))]
    # d = dict()
    # for i in range(len(prices)):
    #     d[i] = 0
    # for i in range(len(prices)):
    #     for j in range(i+1, len(prices)):
    #         d[j] = max(prices[j]-prices[i]+d[i], d[i])
    # return max(list(d.values()))
    if prices is None or len(prices) == 0:
        return 0
    profit = 0
    for i in range(len(prices)-1):
        if prices[i+1] > prices[i]:
            profit += prices[i+1] - prices[i]

    return profit


print(maxProfit([7,1,5,3,6,4]))
