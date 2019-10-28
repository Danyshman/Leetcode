def isPerfectSquare(num):
    result = 0
    i = 1
    while result < num:
        result = i*i
        if result == num:
            return True
        else:
            i += 1
    return False


# print(isPerfectSquare(1))

def judgeSquareSum(self, c: int):
    for i in range(1, c):
        for j in range(1, c):
            if j ** 2 + i ** 2 == c:
                return True
            elif j ** 2 + i ** 2 > c:
                return False


print(judgeSquareSum(4))