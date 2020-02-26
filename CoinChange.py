class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [0 for _ in range(amount + 1)]
        for coin in coins:
            for i in range(1, amount+1):
                if coin == i:
                    dp[i] = 1
                elif coin < i:
                    if dp[i] and dp[i-coin]:
                        dp[i] = min(dp[i], dp[i - coin] + 1)
                    elif dp[i-coin]:
                        dp[i] = dp[i-coin]+1
        return dp[-1] if dp[-1]>0 else -1