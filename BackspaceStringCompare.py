def backspaceCompare(S,T) -> bool:
    i = 0
    while i != len(S):
        if S[i] == '#' and i != 0:
            if i == 0:
                S = S[1:]
                i -= 1
            else:
                S = S[0:i - 1] + S[i + 1:]
                i -= 2
        i += 1
    i = 0
    while i != len(T):
        if T[i] == '#':
            if i == 0:
                T = T[1:]
            else:
                T = T[0:i - 1] + T[i + 1:]
                i -= 2
        i += 1
    return S == T

print(backspaceCompare("a##c","#a#c"))