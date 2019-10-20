def isSubsequence(s,t):
    dp = [False for i in range(len(s))]
    i,j = 0,0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            dp[i] = True
            i += 1
        j += 1
    return (False in dp) is False

print(isSubsequence("","ahbgdc"))