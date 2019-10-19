def firstUniqChar(s):
    d = dict()
    for letter in s:
        d[letter] = d.get(letter, 0) + 1
    index = 0
    for i in range(len(s)):
        if d[s[i]] == 1:
            return i
    return -1

print(firstUniqChar("dddccdbba"))