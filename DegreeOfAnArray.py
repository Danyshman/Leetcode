def findShortestSubArray(nums):
    d = dict()
    max_degree = 0
    ans = len(nums)
    for i in range(len(nums)):
        try:
            d[nums[i]][0] += 1
            d[nums[i]][2] = i
        except Exception:
            d[nums[i]] = [1, i, i]
    for key, value in d.items():
        if value[0] > max_degree:
            ans = value[2] - value[1]
            max_degree = value[0]
        elif value[0] == max_degree and ans > (value[2] - value[1]):
            ans = value[2]- value[1]
    return ans + 1



print(findShortestSubArray([1]))