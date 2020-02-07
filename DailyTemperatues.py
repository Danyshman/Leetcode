def dailyTemperatures(T):
    result = [0] * len(T)
    stack = [(T[-1], len(T) - 1)]
    for i in range(len(T) - 2, -1, -1):
        while True:
            if not stack:
                stack.append((T[i], i))
                break
            elif stack[-1][0] > T[i]:
                result[i] = stack[-1][1] - i
                stack.append((T[i], i))
                break
            else:
                stack.pop()
    return result