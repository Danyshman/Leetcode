def commonChars(A):
    if len(A) == 1:
        return list(A[0])
    answer = []
    flag = True
    for letter in A[0]:
        for i in range(1, len(A)):
            if letter not in A[i]:
                flag = False
                break
        if flag:
            answer.append(letter)
            for i in range(len(A)):
                A[i] = A[i].replace(letter, '', 1)
        flag = True
    return answer


print(commonChars(["cool"]))