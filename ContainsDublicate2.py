def containsNearbyDuplicate(nums,k):
    nums_index = dict()
    for i in range(len(nums)):
        if nums_index.get(nums[i],-1) != -1 and i - nums_index.get(nums[i]) <= k:
            return True
        elif nums_index.get(nums[i],-1) == -1 or i - nums_index.get(nums[i]) > k:
            nums_index[nums[i]] = i
    return False


print(containsNearbyDuplicate(nums = [1,2,3,1], k = 3))