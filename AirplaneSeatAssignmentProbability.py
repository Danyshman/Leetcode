def nthPersonGetsNthSeat(n):
    if n == 1:
        return float(1)
    else:
        return 1/n + (n-2)/n * nthPersonGetsNthSeat(n-1)


print(nthPersonGetsNthSeat(999))