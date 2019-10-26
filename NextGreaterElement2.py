def nextGreaterElements(nums):
    ln = len(nums)
    stack = []
    ans = [-1 for __ in range(ln)]
    for times in range(2):
        for i in range(ln-1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if stack:
                ans[i] = stack[-1]
            stack.append(nums[i])
    return ans


print(nextGreaterElements([-3,2,-2,1,-1,0,-3,-1]))

