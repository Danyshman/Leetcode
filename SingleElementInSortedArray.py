def singleNonDuplicate(nums):
    while len(nums) != 1:
        target = nums[0]
        nums.remove(target)
        try:
            nums.remove(target)
        except Exception:
            return target
    return nums[0]


print(singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
