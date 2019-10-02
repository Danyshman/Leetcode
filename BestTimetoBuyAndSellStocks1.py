def maxProfit(prices):
    if prices is []:
        return 0
    max_profit = 0
    current_min = prices[0]
    for price in prices:
        current_min = min(current_min, price)
        max_profit = max(max_profit, price - current_min)
    return max_profit
