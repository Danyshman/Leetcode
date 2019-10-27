def reverseStr(s, k):
    if k == 1:
        return s
    start = 0
    med = start + k
    end = start + 2*k
    while end <= len(s):
        s = s[:start] + s[start:med][::-1] + s[med:end] + s[end::]
        start = end
        med = start + k
        end = start + 2*k
    if len(s)-1 - start < k:
        s = s[:start] + s[start::][::-1]
        return s
    elif len(s)-1 - end < 2*k:
        s = s[:start] + s[start:med][::-1] + s[start+k::]
        return s


print(reverseStr(s = "krmyfshbspcgtesxnnljhfursyissjnsocgdhgfxubewllxzqhpasguvlrxtkgatzfybprfmmfithphckksnvjkcvnsqgsgosfxc", k=20))