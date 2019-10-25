def findDisappearedNumbers(nums):
    ans = []
    for num in nums:
        if num != 0:
            target = num-1
            while True:
                if nums[target] == 0:
                    break
                else:
                    nums[target], target = 0, nums[target]-1

    for i in range(len(nums)):
        if nums[i] != 0:
            ans.append(i+1)
    return ans


print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))
