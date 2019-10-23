def maxpProfit(prices, fee):
    if len(prices) == 0 or prices is None:
        return 0
    profit = 0
    for i in range(len(prices)-1):
        if (prices[i+1] - prices[i] - fee) > 0:
            profit += prices[i+1] - prices[i] - fee
    return profit


print(maxpProfit(prices = [1, 3, 2, 8, 4, 9], fee = 2))