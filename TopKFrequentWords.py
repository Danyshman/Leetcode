def topKFrequent(words, k):
    d = dict()
    for word in words:
        d[word] = d.get(word, 0) + 1
    d = list(d.items())
    sorted_list = sorted(sorted(d, key=lambda x: (x[0])), key=lambda x: x[1], reverse=True)
    ans = []
    index = 0
    while k > 0:
        ans.append(sorted_list[index][0])
        index += 1
        k -= 1
    return ans


print(topKFrequent(["i", "love", "leetcode", "i", "love", "coding"],3))