def LongestStringChain(words):
    words = sorted(words, key=len)
    print(words)
    d = dict()
    for i in words:
        d[i] = 1
    for i in range(len(words)):
        if len(words[i]) > 1:
            for j in range(len(words[i])):
                target = words[i][:j] + words[i][j+1::]
                d[words[i]] = max(d[words[i]], d.get(target, 0)+1)
    return max(list(d.values()))



print(LongestStringChain(["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"]))