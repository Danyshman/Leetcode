def frequencySort(s):
    d = dict()
    for i in s:
        d[i] = d.get(i, 0) + 1
    sorted_list = sorted(d.items(), key=lambda x:x[1], reverse=True)
    ans = ''
    for i in sorted_list:
        ans = ans + i[0] * i[1]
    return ans



print(frequencySort('Aabb'))