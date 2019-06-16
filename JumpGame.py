def canJump(nums):
    target_index = len(nums)-1
    for i in range(len(nums)-2, -1, -1):
        if (target_index - i) <= nums[i]:
            target_index = i
            continue

    if target_index == 0:
        return True
    else:
        return False


print(canJump([1,0,2,0,0]))