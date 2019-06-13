def solution(nums, target):
    for i in range(len(nums)):
        if (target - nums[i]) in (nums[0:i] + nums[i+1::]):
            for j in range(i+1,len(nums)):
                if nums[j] == (target-nums[i]):
                    return [i, j]


print(solution([3,2,4],6))
