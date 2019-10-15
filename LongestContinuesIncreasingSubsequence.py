def findLengthOfCIS(nums):
    max_len = 0
    for i in range(len(nums)):
        temp_len = 1
        target = nums[i]
        for j in range(i+1, len(nums)):
            if nums[j] > target:
                temp_len += 1
                target = nums[j]
            else:
                break
        if temp_len > max_len:
            max_len = temp_len
    return max_len


print(findLengthOfCIS([1]))
