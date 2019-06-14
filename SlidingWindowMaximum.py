def maxSlidingWindow(nums, k):
    if nums == []:
        return []
    max_nums = []
    for i in range(len(nums)-k+1):
        max_nums.append(max(nums[i:i+k]))
    return max_nums


print(maxSlidingWindow(nums=[], k=0))