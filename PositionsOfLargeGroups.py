def largeGroupsPositions(S):
    start = 0
    sum = 1
    target = S[0]
    ans = []
    for i in range(1, len(S)):
        if S[i] == target:
            sum += 1
        if S[i] != target and sum >= 3:
            ans.append([start, i-1])
            start = i
            target = S[i]
            sum = 1
        if S[i] != target and sum < 3:
            start = i
            target = S[i]
            sum = 1
        if i == len(S)-1 and sum >= 3 and S[-1]==target:
            ans.append([start, i])
    return ans


print(largeGroupsPositions("aaa"))