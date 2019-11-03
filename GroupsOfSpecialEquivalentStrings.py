def numSpecialEquivGroups(A):
    ans = set()
    for i in range(len(A)):
        even_letters = []
        odd_letters = []
        if len(A) == 1:
            odd_letters.append(A[i])
        else:
            for j in range(0,len(A[i]), 2):
                even_letters.append(A[i][j])
            for j in range(1, len(A[i]), 2):
                odd_letters.append(A[i][j])
        even_letters.sort()
        odd_letters.sort()
        ans.add((tuple(even_letters), tuple(odd_letters)))
    return len(ans)


print(numSpecialEquivGroups(["abc","acb","bac","bca","cab","cba"]))