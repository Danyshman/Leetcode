def findDuplicates(nums):
    duplicates = []
    unique_values = set()
    for num in nums:
        previous_len_uniue_val = len(unique_values)
        unique_values.add(num)
        curr_len_unique_val = len(unique_values)
        if curr_len_unique_val == previous_len_uniue_val:
            duplicates.append(num)
    return duplicates


print(findDuplicates1([4,3,2,7,8,2,3,1]))