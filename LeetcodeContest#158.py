def balancedStringSplit(s):
    ans = 0
    l = 0
    r = 0
    for i in s:
        if l == r:
            ans += 1
            l = 0
            r = 0
        if i == "L":
            l += 1
        if i == 'R':
            r += 1

    return ans


# print(balancedStringSplit("LLLLRRRR"))



def queensAttacktheKing(queens, king):
    ans = []
    king_row = king[0]
    king_col = king[1]
    for i in range(king_row, -1, -1):
        if [i, king_col] in queens:
            ans.append([i, king_col])
            break
    for i in range(king_row, 8):
        if [i, king_col] in queens:
            ans.append([i, king_col])
            break
    for i in range(king_col, -1, -1):
        if [king_row, i] in queens:
            ans.append([king_row, i])
            break
    for i in range(king_col, 8):
        if [king_row, i] in queens:
            ans.append([king_row, i])
            break
    a = king_row
    b= king_col
    while a >= 0 and b >= 0:
        if [a,b] in queens:
            ans.append([a,b])
            break
        else:
            a -= 1
            b -= 1
    a = king_row
    b = king_col
    while a < 8 and b < 8:
        if [a,b] in queens:
            ans.append([a,b])
            break
        else:
            a += 1
            b += 1
    a = king_row
    b = king_col
    while a >= 0 and b < 8:
        if [a,b] in queens:
            ans.append([a,b])
            break
        else:
            a -= 1
            b += 1
    a = king_row
    b = king_col
    while a < 8 and b >= 0:
        if [a, b] in queens:
            ans.append([a, b])
            break
        else:
            a += 1
            b -= 1
    return ans


def maxEqualFreq(nums):
    d = dict()
    for num in nums:
        d[num] = d.get(num, 0) + 1
    temp = set(d.values())
    if len(temp) == 2 and (1 in temp):
        return len(nums)
    for i in range(len(nums)-1, -1, -1):
        d[nums[i]] -= 1
        temp = set(d.values())

    return 0


print(maxEqualFreq([10,2,8,9,3,8,1,5,2,3,7,6]))


