def searchRange(nums, target):
    left = 0
    right = len(nums)-1
    flag = False
    index = -1
    result = [-1, -1]
    while left <= right:
        med = (left + right) // 2
        if nums[med] == target:
            flag = True
            index = med
            break
        elif target > nums[med]:
            left = med + 1
        else:
            right = med - 1
    if flag:
        left = index
        right = index
        while left >= 0 and nums[left]==nums[index]:
            result[0] = left
            left -= 1
        while right < len(nums) and nums[right]==nums[index]:
            result[1] = right
            right += 1
        return result
    else:
        return result


print(searchRange([1,4], 4))