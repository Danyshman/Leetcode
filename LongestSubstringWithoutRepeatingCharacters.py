def lengthOfLongestSubstring(s):
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    if s[0] * len(s) == s:
        return 1
    longest_substring = ''
    for i in range(len(s)):
        char_indexes = dict()
        char_indexes[s[i]] = True
        temp = s[i]
        for j in range(i+1, len(s)):
            if char_indexes.get(s[j], False) is False and j == len(s)-1 and len(temp)+1 > len(longest_substring):
                longest_substring = temp + s[j]
            if char_indexes.get(s[j], False):
                if len(temp) > len(longest_substring):
                    longest_substring = temp
                break
            else:
                char_indexes[s[j]] = True
                temp += s[j]
    return len(longest_substring)


print(lengthOfLongestSubstring("tmmzuxt"))