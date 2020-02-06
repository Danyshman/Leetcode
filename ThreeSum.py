def threeSum(nums):
    result = set()
    nums.sort()
    for i in range(len(nums)):
        l = i+1
        r = len(nums)-1
        while l < r:
            temp_val = nums[i]+nums[l]+nums[r]
            if temp_val == 0:
                result.add((nums[i],nums[l],nums[r]))
                l += 1
                r -= 1
            elif temp_val > 0:
                r -= 1
            else:
                l += 1
    return list(result)


print(threeSum([-1, 0, 1, 2, -1, -4]))
