def thirdMax(nums):
    if len(set(nums)) < 3:
        return max(nums)
    nums = list(set(nums))
    nums.sort()
    return nums[-3]