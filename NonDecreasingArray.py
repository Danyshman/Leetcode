def checkPossibility(nums):
    diff = 0
    for i in range(len(nums) - 1):
        if nums[i] > nums[i+1]:
            diff += 1
            v1= nums[:i] + nums[i+1::]
            v2 = nums[:i+1] + nums[i+2::]
            if v1 != sorted(v1) and v2 != (sorted(v2)):
                return False
        if diff > 1:
            return False
    return True


print(checkPossibility([4,2,1]))