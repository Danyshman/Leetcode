def findUnsortedSubarray(nums):
    sorted_nums = sorted(nums)
    if sorted_nums == nums:
        return 0
    l = 0
    r = len(nums)-1
    while nums[l] == sorted_nums[l] or nums[r] == sorted_nums[r]:
        if nums[l] == sorted_nums[l]:
            l += 1
        if nums[r] == sorted_nums[r]:
            r -= 1

    return r-l+1

print(findUnsortedSubarray([1,3,2,4,5]))
