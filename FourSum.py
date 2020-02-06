def fourSum(nums, target):
    result = set()
    nums.sort()
    for i in range(len(nums)-3):
        for j in range(i+1, len(nums)-2):
            l = j + 1
            r = len(nums)-1
            while l < r:
                temp_val = nums[i] + nums[j] + nums[l] + nums[r]
                if temp_val == target:
                    result.add((nums[i], nums[j], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif temp_val > target:
                    r -= 1
                else:
                    l += 1
    return list(result)


print(fourSum([-1,0,1,2,-1,-4], -1))