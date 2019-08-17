def productExceptSelf(nums):
    length = len(nums)
    L, R, answer = [0]*len(nums),  [0]*len(nums), [0]*len(nums)
    L[0] = 1
    R[length - 1] = 1
    length -= 2
    for i in range(1, len(nums)):
        L[i] = nums[i-1] * L[i-1]
        R[length] = nums[length + 1] * R[length + 1]
        length -= 1
    for i in range(len(answer)):
        answer[i] = L[i]*R[i]
    return answer


print(productExceptSelf([1,2,3,4]))