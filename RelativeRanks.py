def findRelativeRanks(nums):
    sort_nums = nums.copy()
    sort_nums.sort()
    sort_nums = sort_nums[::-1]
    temp = 4
    for i in range(len(sort_nums)):
        if i == 0:
            nums[nums.index(sort_nums[i])] = 'Gold Medal'
        elif i == 1:
            nums[nums.index(sort_nums[i])] = 'Silver Medal'
        elif i == 2:
            nums[nums.index(sort_nums[i])] = 'Bronze Medal'
        else:
            nums[nums.index(sort_nums[i])] = str(temp)
            temp += 1
    return nums


print(findRelativeRanks([1]))