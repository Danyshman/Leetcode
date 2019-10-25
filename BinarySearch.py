def search(nums, target):
    start = 0
    end = len(nums)-1
    if len(nums) == 1 and nums[0] == target:
        return 0
    elif len(nums) == 1 and nums[0] != target:
        return -1
    while start != end:
        med = (start+end)//2+1
        if nums[med] == target:
            return med
        elif nums[med] > target:
            end = med-1
        else:
            start = med
    if nums[start] == nums[end] == target:
        return start
    else:
        return -1


print(search([-1,5], 5))