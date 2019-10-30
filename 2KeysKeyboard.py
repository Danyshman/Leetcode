def check_prime(n):
    if n == 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def minSteps(n):
    count = 0
    while n != 3 and n != 5 and n != 2:
        is_prime = check_prime(n)
        if is_prime:
            count += n
            return count
        else:
            for i in range(n//2, 1, -1):
                if n % i == 0:
                    count += n // i
                    n = i
                    break
    if n == 2:
        count += 2
    elif n == 3:
        count += 3
    elif n == 5:
        count += 5
    return count


print(minSteps(6))
