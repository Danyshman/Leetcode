def searchInsert(nums, target):
    if nums[-1] < target:
        return len(nums)
    for i in range(len(nums)):
        if nums[i] > target or nums[i] == target:
            return i
