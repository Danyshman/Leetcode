def findMaxConsecutiveOnes(nums):
    max = 0
    count = 0
    target = 1
    for i in range(len(nums)):
        if nums[i] == target:
            count += 1
        else:
            if count > max:
                max = count
                count = 0
            else:
                count = 0
    if count > max:
        max = count
    return max


print(findMaxConsecutiveOnes([1,0,1,1,0,1]))