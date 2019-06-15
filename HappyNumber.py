def isHappy(n):
    for i in range(100):
        new_num = 0
        for digit in str(n):
            new_num += int(digit)**2
        if new_num == 1:
            return True
        n = new_num
    return False

print(isHappy(19))