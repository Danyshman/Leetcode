def removeDuplicates(nums):
    for num in nums:
        for i in range(nums.count(num)-1):
            nums.remove(num)
    return len(nums)

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
