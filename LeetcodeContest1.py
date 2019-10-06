def minCostToMoveChips(chips):
    sum = 0
    even = 0
    odd = 0
    for i in range(len(chips)):
        if chips[i] % 2 == 0:
            even += 1
        else:
            odd += 1
    return min(even, odd)


print(minCostToMoveChips([6,4,7,8,2,10,2,7,9,7]))


def longestSubsequence(arr, difference):
    max_subseq = 1
    arr1 = set(arr)
    checked_nums = set()
    for i in range(len(arr)-1):
        if arr[i] in checked_nums:
            continue
        target = arr[i] + difference
        temp_max = 1
        if target not in arr1:
            continue
        checked_nums.add(arr[i])
        for j in range(i+1,len(arr)):
            if target not in arr1:
                break
            if arr[j] == target:
                checked_nums.add(target)
                target += difference
                temp_max += 1
        if temp_max > max_subseq:
            max_subseq = temp_max
    return max_subseq


# print(longestSubsequence([1,5,7,8,5,3,4,2,1], -2))

