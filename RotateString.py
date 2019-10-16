def rotateString(A, B):
    if A == B:
        return True
    if A != B and A == '':
        return False
    first_letter = B[0]
    for i in range(len(A)):
        if A[i] == first_letter:
            if B == (A[i::] + A[:i]):
                return True
    return False


print(rotateString(A = 'abcde', B = 'abced'))
