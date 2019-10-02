import math


def fib(N):
    sqroot5 = math.sqrt(5)
    phi = (1+sqroot5)/2
    return round((math.pow(phi, N)-math.pow(-phi, -N))/sqroot5)


print(fib(5))