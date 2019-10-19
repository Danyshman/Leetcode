def isPowerOfFour(num):
    bin_num = str(bin(num))[2:]
    print(bin_num)
    if bin_num[0] == '1' and ('0'*(len(bin_num)-1) == bin_num[1::]) and (len(bin_num) % 2 == 1):
        return True
    else:
        return False


print(isPowerOfFour(5))