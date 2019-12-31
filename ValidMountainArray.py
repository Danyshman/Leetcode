import numpy as np


def validMountainArray(A):
    if len(A) < 3:
        return False
    A = np.array(A)
    max_num_index = A.argmax()
    if max_num_index == 0 or max_num_index == len(A)-1:
        return False
    left_ind, right_ind = max_num_index-1, max_num_index+1
    for i in range(left_ind, -1, -1):
        if A[i] >= A[i+1]:
            return False
    for i in range(right_ind, len(A)):
        if A[i] >= A[i-1]:
            return False
    return True


print(validMountainArray([0,1,2,1,2]))

