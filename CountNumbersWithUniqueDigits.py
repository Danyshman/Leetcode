def countNumbersWithUniqueDigits(n):
    unique_vals = [10, 81, 648, 4536, 27216, 136080, 544320,1632960, 3265920, 3265920]
    if n > 10:
        n = 10
    return sum(unique_vals[:n])





print(countNumbersWithUniqueDigits(11))