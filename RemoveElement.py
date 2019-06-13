def removeElement(nums, val):
    for i in range(nums.count(val)):
        nums.remove(val)
    return len(nums)