def search(nums, target):
    left = 0
    right = len(nums)-1
    while left <= right:
        med = (left + right) // 2
        if nums[med] == target:
            return med
        elif nums[med] > target:
            right = med - 1
        elif nums[med] < target:
            left = med + 1
    return - 1


print(search([1,4,5,3,1], 5))