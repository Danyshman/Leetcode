def topKFrequent(nums, k):
    d = dict()
    for num in nums:
        d[num] = d.get(num, 0) + 1

    ans = []
    index = -1
    d = sorted(d.items(), key=lambda x: x[1])
    while k > 0:
        ans.append(d[index][0])
        index -= 1
        k -= 1
    return ans


print(topKFrequent([3,0,1,0],1))
