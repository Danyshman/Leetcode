def relativeSortArray(arr1, arr2):
    result = []
    excluded_nums = []
    for num in arr1:
        if num not in arr2:
            excluded_nums.append(num)
    excluded_nums.sort()
    excluded_nums.sort()
    for num in arr2:
        count_of_n = arr1.count(num)
        for i in range(count_of_n):
            result.append(num)
    for num in excluded_nums:
        result.append(num)
    return result


print(relativeSortArray(arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]))
