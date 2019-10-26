def diStringMatch(S):
    min_num = 0
    max_num = len(S)
    ans = []
    for i in S:
        if i == 'I':
            ans.append(min_num)
            min_num += 1
        elif i == 'D':
            ans.append(max_num)
            max_num -= 1
    return ans + [max_num]


print(diStringMatch("III"))