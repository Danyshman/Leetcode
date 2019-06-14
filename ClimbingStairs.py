def climbingStairs(n):
    a = 1
    b = 2
    if n == 1:
        return a
    elif n == 2:
        return 2
    else:
        for i in range(n - 2):
            c = a + b
            a = b
            b = c
        return c
