def findAndReplacePattern(words, pattern):
    ans= []
    for i in range(len(words)):
        if len(words[i]) != len(pattern):
            continue
        word_val = dict()
        pattern_val = dict()
        is_match = True
        for j in range(len(pattern)):
            word_val[words[i][j]] = word_val.get(words[i][j], 0) + 1
            pattern_val[pattern[j]] = pattern_val.get(pattern[j], 0) + 1
            if list(word_val.values()) != list(pattern_val.values()):
                is_match = False
                break
        if is_match:
            ans.append(words[i])
    return ans


print(findAndReplacePattern(words = ["abc], pattern = "abb"))