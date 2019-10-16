def longestWord(words):
    words.sort()
    d = dict()
    for word in words:
        if len(word) == 1:
            d[word] = True
        else:
            temp = d.get(word[:-1],False)
            if temp:
                d[word] = True
    ans = ''
    for i in d.keys():
        if len(i) > len(ans):
            ans = i
        elif len(i) == len(ans) and i < ans:
            ans = i
    return ans


print(longestWord(["yo","ew","fc","zrc","yodn","fcm","qm","qmo","fcmz","z","ewq","yod","ewqz","y"]))

print('z' < 'yodn')