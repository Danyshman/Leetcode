def letterCasePermuation(S):
    nums = '0123456789'
    d = []
    for i in range(len(S)):
        if S[i] not in nums:
            d.append((S[i].lower(),i))
    ans = set()
    S=S.lower()
    for key,val in d:
        temp = ans.copy()
        if len(ans) == 0:
            l = S[:val] + S[val].lower() + S[val + 1::]
            h = S[:val] + S[val].upper() + S[val + 1::]
            ans.add(l)
            ans.add(h)
        else:
            for i in ans:
                l = i[:val] + i[val].lower() + i[val+1::]
                h = i[:val] + i[val].upper() + i[val+1::]
                temp.add(l)
                temp.add(h)
            ans = temp
    if len(ans) == 0:
        return [S]
    else:
        return list(ans)


print(letterCasePermuation("RmR"))

