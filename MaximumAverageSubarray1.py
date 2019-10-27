def findMaxAverage(nums, k):
    max_avg = sum(nums[:k])/k
    last_sum = sum(nums[:k])
    start = 0
    for i in range(k, len(nums)):
        last_sum -= nums[start]
        start += 1
        last_sum += nums[i]
        max_avg = max(max_avg, last_sum/k)
    return max_avg


print(findMaxAverage([1,12,-5,-6,50,3], 4))
