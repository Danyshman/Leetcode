def removeDuplicates(S):
    is_there_duplicate = True
    i = 0
    while (i != len(S)-1) and len(S) != 0:
        if S[i] == S[i + 1]:
            S = S[:i] + S[i + 2::]
            if i != 0:
                i -= 1
            continue
        i+= 1
    return S


print(removeDuplicates("aaaaaaaa"))
