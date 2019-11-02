def buddyStrings(A, B):
    if len(A) != len(B) or len(A) < 2 or len(B) < 2:
        return False
    a_equal_b = A == B
    count_val = dict()
    if a_equal_b:
        for i in A:
            if count_val.get(i, False):
                return True
            else:
                count_val[i] = True
    diff_val = []
    for i in range(len(A)):
        if A[i] != B[i]:
            diff_val.append(A[i])
            diff_val.append(B[i])
    if len(diff_val) != 4:
        return False
    return diff_val == diff_val[::-1]



print(buddyStrings("abab", "abab"))