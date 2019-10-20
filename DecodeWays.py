def numDecodings(s):
    dp = [0 for i in range(len(s)+1)]
    dp[0] = 1
    if s[0] == '0':
        dp[1] = 0
    else:
        dp[1] = 1
    for i in range(2, len(s)+1):
        one_digit = int(s[i-1:i])
        two_digit = int(s[i-2:i])
        if one_digit >= 1:
            dp[i] += dp[i-1]
        if 10 <= two_digit <= 26:
            dp[i] += dp[i-2]
    return dp[len(s)]


print(numDecodings('12'))