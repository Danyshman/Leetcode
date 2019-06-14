def singleNumber(nums):
    while True:
        num = nums[0]
        nums.remove(nums[0])
        if num not in nums:
            return num
        else:
            nums.remove(num)

print(singleNumber([2,2,1]))