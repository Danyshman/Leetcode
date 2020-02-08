def mirrorize(string, n):
    if n > len(string)-1:
        return string
    result = string[0:n-1]
    for i in range(n-1, len(string)):
        result += chr(ord('a')+(25-(ord(string[i])-ord('a'))))
    return result


print(mirrorize('paradox', 3))
