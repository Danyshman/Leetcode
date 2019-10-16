def longestPalindrome(s):
    if s[0]*len(s) == s:
        return len(s)
    d = dict()
    for i in s:
        d[i] = d.get(i, 0) + 1
    values = list(d.values())
    values.sort()
    max_len = 0
    i = len(values)-1
    while i >= 0:
        if values[i] % 2 == 0:
            max_len += values[i]
            i -= 1
        elif values[i] % 2 == 1 and values[i] != 1:
            max_len += values[i]-1
            values.insert(0, 1)
        else:
            max_len += values[i]
            break
    return max_len


print(longestPalindrome("ababababa"))
