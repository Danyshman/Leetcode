def repeatedSubstringPattern(s):
    for i in range(len(s)-1):
        if len(s) % (i+1) == 0 and s[:i+1]*(len(s)//len(s[:i+1])) == s:
            return True
    return False


print(repeatedSubstringPattern("abcabcabcabc"))