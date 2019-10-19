def isPowerOfThree(n):
    n_pow = 0
    while pow(3, n_pow) <= n:
        if pow(3, n_pow) == n:
            return True
        else:
            n_pow += 1
    return False


print(isPowerOfThree(243))