import math
def uniquePaths(m,n):
    fm = math.factorial(m - 1)
    fn = math.factorial(n - 1)
    fmn = math.factorial(m + n - 2)
    return int(fmn / (fn * fm))



print(uniquePaths(3,2))
