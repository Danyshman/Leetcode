def isAlienSorted(words, order):
    d = {}
    for i in range(len(order)):
        d[order[i]] = i
    if len(words) == 1:
        return True
    for i in range(len(words)-1):
        word1 = words[i]
        word2 = words[i+1]
        if word2 in word1 and len(word2) < len(word1):
            return False
        for j in range(len(word1)):
            if d[word1[j]] > d[word2[j]]:
                return False
            elif d[word1[j]] < d[word2[j]]:
                break
            else:
                continue
    return True


print(isAlienSorted(words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"))
