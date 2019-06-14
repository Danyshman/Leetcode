import string
import math
def convertToTitle(n):
    base = list(string.ascii_uppercase[0:26])
    if n <= 26:
        return base[n-1]
    else:
        isTrue = False
        result = ''
        while n > 26:
            if isTrue:
                result = base[(n % 26) - 2] + result
                isTrue = False
            else:
                result = base[(n % 26) - 1] + result
            if n%26==0:
                isTrue = True
            n = math.floor(n/26)
        if isTrue:
            result = base[n-2] + result
        else:
            result = base[n-1] + result
        return result



print(convertToTitle(702))