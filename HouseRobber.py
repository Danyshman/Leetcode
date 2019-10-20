def rob(nums):
    if 0<len(nums) <= 2:
        return max(nums)
    if len(nums) == 0:
        return 0
    dp = [0 for i in range(len(nums))]
    dp[0] = nums[0]
    dp[1] = nums[1]
    dp[2] = dp[0] + nums[2]
    for i in range(3, len(nums)):
        dp[i] = max(dp[i-3], dp[i-2]) + nums[i]
    return max(dp)





print(rob([0]))