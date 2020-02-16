def removeDuplicates(s,k) -> str:
    st = []
    i = 0
    while i < len(s):
        a = s[i - k + 1:i + 1]
        if i >= k-1 and s[i - k:i + 1] == s[i] * k-1:
            s = s[:i - k] + s[i + 1:]
            i -= k
            continue
        i += 1
    return ''.join(st)

print(removeDuplicates(s = "deeedbbcccbdaa", k = 3))