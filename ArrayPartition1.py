def arrayPairSum(nums):
    n = int(len(nums)/2)
    nums.sort()
    sum = 0
    for i in range(0,len(nums),int(len(nums)/n)):
        sum += nums[i]
    return sum


print(arrayPairSum([1,4,3,2]))