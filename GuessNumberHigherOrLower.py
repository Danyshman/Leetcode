def guessNumber(n):
    left = 1
    right = n
    while left <= right:
        mid = (left + right) // 2
        temp = guess(mid)
        if temp == -1:
            right = mid -1
        elif temp == 1:
            left = mid + 1
        else:
            return mid