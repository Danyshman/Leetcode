def singleNumber(nums):
    return_arr = []
    while True:
        num = nums[0]
        nums.remove(num)
        if num not in nums:
            return_arr.append(num)
            if len(return_arr) == 2:
                return return_arr
        else:
            nums.remove(num)


print(singleNumber([1,2,1,3,2,5]))

