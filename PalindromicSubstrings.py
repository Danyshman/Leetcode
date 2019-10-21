def countingSubstrings(s):
    # dp = [[False for __ in range(len(s))] for __ in range(len(s))]
    # for i in range(len(dp)):
    #     dp[i][i] = True
    count = len(s)
    for i in range(len(s)-1):
        for j in range(i+1,len(s)):
            if s[i:j+1] == s[i:j+1][::-1]:
                count += 1
    return count

print(countingSubstrings('ajkasb'))