def fairCandySwap(A,B):
    sum_a = sum(A)
    sum_b = sum(B)
    ans = [0,0]
    while sum_a != sum_b:
        diff = abs(sum_a- sum_b)//2
        if sum_b > sum_a:
            for i in range(len(B)):
                if B[i] >= diff:
                    ans[1] += B[i]
                    sum_b -= B[i]
                    A.append(B[i])
                    A.sort()
                    sum_a += B[i]
                    B = B[:i] + B[i+1::]
                    break

        else:
            for i in range(len(A)):
                if A[i] >= diff:
                    ans[0] += A[i]
                    sum_a -= A[i]
                    B.append(A[i])
                    B.sort()
                    sum_b += A[i]
                    A = A[:i] + A[i+1::]
                    break
    return ans


print(fairCandySwap([2], [1,3]))

