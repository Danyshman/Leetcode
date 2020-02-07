def hammingWeight(n):
    str_num = bin(n)[2:]
    count = 0
    for num in str_num:
        if num == '1':
            count += 1
    return count