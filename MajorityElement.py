def majorityElement(nums):
    was_checked = []
    for num in nums:
        if num in was_checked:
            continue
        else:
            if nums.count(num) > len(nums)//2:
                return num
            was_checked.append(num)


print(majorityElement([2,2,1,1,1,2,2]))