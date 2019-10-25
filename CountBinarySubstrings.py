def countBinarySubstrings(s):
    count = 0
    for i in range(len(s)-1):
        if s[i:i+2] == '01' or s[i:i+2] == '10':
            count += 1
            start = i-1
            end = i+2
            while len(s) > end and start >= 0:
                if s[start] == s[i] and s[end] == s[i+1]:
                    count += 1
                    start -= 1
                    end += 1
                else:
                    break
    return count


print(countBinarySubstrings("10"))
