def minCostTickets(days, costs):
    dp = [False for __ in range(days[-1]+1)]
    dp[0] = 0
    for day in days:
        dp[day] = True
    for i in range(1, len(dp)):
        if dp[i] is False:
            dp[i] = dp[i-1]
        else:
            one = dp[i-1] + costs[0]
            seven = dp[max(i-7, 0)] + costs[1]
            thirty = dp[max(i-30, 0)] + costs[2]
            dp[i] = min(one,seven, thirty)
    return dp[-1]


print(minCostTickets(days = [1,4,6,7,8,20], costs = [2,7,15]))
