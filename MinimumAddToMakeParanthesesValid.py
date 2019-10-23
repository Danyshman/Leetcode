def minAddToMakeValid(S):
    count = 0
    open = 0
    close = 0
    for i in S:
        if i == '(':
            open += 1
        elif i == ')':
            close += 1
        if close > open:
            open += 1
            count += 1
    if open == close:
        return count
    else:
        return count + (open-close)


print(minAddToMakeValid("()))(("))