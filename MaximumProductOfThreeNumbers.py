def maximumProduct(nums):
    nums.sort()
    return max([nums[0] * nums[1] * nums[2], nums[0] * nums[1] * nums[-1], nums[0]*nums[-1],nums[-2],nums[-1]*nums[-2]*nums[-3]])


print(maximumProduct([-1,-2,-3]))