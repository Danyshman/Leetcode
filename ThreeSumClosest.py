def threeSumClosest(nums, target):
    closest = sum(nums[:3])
    nums.sort()
    for i in range(len(nums)):
        l = i + 1
        r = len(nums) - 1
        while l < r:
            temp_var = nums[i] + nums[l] + nums[r]
            if abs(temp_var - target) < abs(closest - target):
                closest = temp_var
            if temp_var == target:
                return temp_var
            elif temp_var > target:
                r -= 1
            else:
                l += 1
    return closest


print(threeSumClosest([-1, 2, 1, -4], 1))