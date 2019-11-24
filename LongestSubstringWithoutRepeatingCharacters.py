def lengthOfLongestSubstring(self, s: str) -> int:
    global_max = temp_max = start = 0
    d = dict()
    for index, letter in enumerate(s):
        if letter in d and d[letter] >= start:
            global_max = max(global_max, temp_max)
            temp_max = index - d[letter]
            start = d[letter] + 1
        else:
            temp_max += 1
        d[letter] = index
    return max(global_max, temp_max)


print(lengthOfLongestSubstring("pwwkew"))