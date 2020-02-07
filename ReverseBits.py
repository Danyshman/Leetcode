def reverseBits(n):
    str_n = str(bin(n))[2:]
    str_n = '0' * (32 - len(str_n)) + str_n
    str_n = str_n[::-1]
    return int(str_n, 2)


print(reverseBits(43261596))