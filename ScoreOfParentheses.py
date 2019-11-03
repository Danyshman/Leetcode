def scoreOfParantheses(S):
    temp = list(S)
    i = 0
    while i < len(temp) - 1:
        if temp[i] == '(' and temp[i + 1] == ')':
            temp = temp[:i] + ['1'] + temp[i + 2::]
        else:
            i += 1
    if len(temp) == 1:
        return int(temp[0])
    while '(' in temp or len(temp) > 1:
        i = 1
        while len(temp) - 1 > i:
            if temp[i] not in '()' and temp[i - 1] == '(' and temp[i + 1] == ')':
                temp = temp[:i - 1] + [str(2 * int(temp[i]))] + temp[i + 2::]
                i -= 1
            else:
                i += 1
        i = 0
        while i < len(temp) - 1:
            if temp[i] not in '()' and temp[i + 1] not in '()':
                temp = temp[:i] + [str(int(temp[i]) + int(temp[i + 1]))] + temp[i + 2::]
            else:
                i += 1
        S = ''.join(temp)
    return int(S)


print(scoreOfParantheses("(()(()))"))
