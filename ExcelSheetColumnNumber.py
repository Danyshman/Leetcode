def titleToNumber(s):
    total = 0
    len_s = len(s)-1
    for char in s:
        total += (pow(26,len_s)) * (ord(char)-64)
        len_s -= 1

    return total


print(titleToNumber('AB'))