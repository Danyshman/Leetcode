def findPairs(nums, k):
    ans = set()
    past_nums = dict()
    for i in range(len(nums)):
        if past_nums.get(nums[i]-k,False) and ((nums[i], nums[i]-k) not in ans) and ((nums[i]-k, nums[i]) not in ans):
            ans.add((nums[i], nums[i]-k))
            past_nums[nums[i]] = True
        if past_nums.get(nums[i] + k, False) and ((nums[i], nums[i]+k) not in ans) and ((nums[i]+k, nums[i]) not in ans):
            ans.add((nums[i], nums[i]+k))
            past_nums[nums[i]] = True
        else:
            past_nums[nums[i]] = True
    return len(ans)


print(findPairs([6,3,5,7,2,3,3,8,2,4], 2))

