def singleNumber(nums):
    while True:
        num = nums[0]
        nums.remove(num)
        try:
            nums.remove(num)
        except Exception:
            return num
        if num not in nums:
            return num
        else:
            nums.remove(num)

