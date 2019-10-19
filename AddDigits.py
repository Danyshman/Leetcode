def addDigits(num):
    new_num = 0
    while len(str(num)) != 1:
        for n in str(num):
            new_num += int(n)
        num = new_num
        new_num = 0
    return num


print(addDigits(38))