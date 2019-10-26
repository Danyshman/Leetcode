def findErrorNums(nums):
    d = dict()
    for i in range(1, len(nums)+1):
        d[i] = 0
    for i in range(len(nums)):
        d[nums[i]] += 1
    ans = [0, 0]
    for key,val in d.items():
        if val > 1:
            ans[0] = key
        elif val == 0:
            ans[1] = key
    return ans

print(findErrorNums([1,2,2,4]))