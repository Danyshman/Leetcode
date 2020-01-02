def sortArrayByParitII(A):
    even_nums = []
    odd_nums = []
    for num in A:
        if num%2==0:
            even_nums.append(num)
        else:
            odd_nums.append(num)
    n = len(A)
    A.clear()
    even_ind = odd_ind = 0
    for i in range(n):
        if i%2==0:
            A.append(even_nums[even_ind])
            even_ind += 1
        else:
            A.append(odd_nums[odd_ind])
            odd_ind += 1
    return A

