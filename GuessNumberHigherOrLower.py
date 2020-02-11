def guessNumber(n):
    left = 1
    right = n
    while left <= right:
        mid = (left + right) // 2
        guess = self.guess(mid)
        if guess == -1:
            right = mid -1
        elif guess == 1:
            left = mid + 1
        else:
            return mid