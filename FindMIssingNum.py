def missingNumber(nums):
    max_num = len(nums)
    true_sum = ((max_num+1)*max_num)/2
    false_sum = sum(nums)
    missing_num = int(true_sum-false_sum)
    return missing_num


print(missingNumber([0]))
