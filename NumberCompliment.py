def findComplement(num):
    bin_num = bin(num)
    str_bin_num = str(bin_num)[2::]
    result_num = ''
    for i in range(len(str_bin_num)):
        if str_bin_num[i] == '0':
            result_num += '1'
        else:
            result_num += '0'
    return int(result_num, 2)



print(findComplement(5))