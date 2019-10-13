def addToArrayForm(A,K):
    num = ''
    for i in A:
        num += str(i)
    num2 = int(num) + K
    return list(str(num2))


print(addToArrayForm(A = [1,2,0,0], K = 34))