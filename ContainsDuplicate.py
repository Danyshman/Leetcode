def containsDuplicate(nums):
    unique_nums = set(nums)
    if len(nums) == len(unique_nums):
        return False
    else:
        return True


print(containsDuplicate([1,2,3,4]))