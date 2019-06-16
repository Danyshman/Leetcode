def sortedSquares(A):
    square_arr = []
    for num in A:
        square_arr.append(num**2)
    square_arr.sort()
    return square_arr