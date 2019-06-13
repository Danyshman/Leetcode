def strStr(haystack, needle):
    if needle not in haystack:
        return -1
    if needle == '':
        return 0
    if needle == haystack:
        return 0
    for i in range(len(haystack)-len(needle)+1):
        print(haystack[i:i+len(needle)])
        if haystack[i:i+len(needle)] == needle:
            return i

print(strStr("mississippi","pi"))