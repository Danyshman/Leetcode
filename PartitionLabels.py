def partitionLabels(S):
    d = {}
    for i, c in enumerate(S):
        d[c] = i
    start = 0
    end = 0
    ans = []
    for i, c in enumerate(S):
        end = max(end, d[c])
        if end == i:
            ans.append(end - start + 1)
            start = end + 1
    return ans


print(partitionLabels('ababcbacadefegdehijhklij'))