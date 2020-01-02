import numpy as np


def transpose(A):
    A = np.array(A)
    A=A.transpose()
    return A


print(transpose([[1,2,3],[4,5,6],[7,8,9]]))