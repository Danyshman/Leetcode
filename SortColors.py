def sortColors(nums):
    zero = one = two = 0
    for i in nums:
        if i == 0:
            zero += 1
        elif i == 1:
            one += 1
        else:
            two += 1
    index = 0
    for i in range(zero):
        nums[index] = 0
        index += 1
    for i in range(one):
        nums[index] = 1
        index += 1
    for i in range(two):
        nums[index] = 2
        index += 1
    return nums

print(sortColors([0]))