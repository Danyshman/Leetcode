def isUgly(num):
    if num == 0:
        return False
    while num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
        if num % 2 == 0:
            num /= 2
        elif num % 3 == 0:
            num /= 3
        elif num % 5 == 0:
            num /= 5
    if num == 1:
        return True
    else:
        return False


print(isUgly(55))