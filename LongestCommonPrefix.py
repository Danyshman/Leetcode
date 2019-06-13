def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ''
    if len(strs) == 1:
        return strs[0]
    longest_common_prefix = ''
    first_word = strs[0]
    for i in range(len(first_word)):
        if isThere(strs, i+1):
            longest_common_prefix = first_word[0:i+1]
    return longest_common_prefix


def isThere(strs, stop):
    for word in strs:
        if strs[0][0:stop] != word[0:stop]:
            return False
    return True


print(longestCommonPrefix(["flower","flow","flight"]))

