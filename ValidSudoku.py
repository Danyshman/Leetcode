import numpy as np

def isValidSudoku(board):
    board = np.array(board)
    if not check_row_and_col(board):
        return False
    for r_s in range(0, 9, 3):
        for c_s in range(0, 9, 3):
            r_e = r_s + 3
            c_e = c_s + 3
            all_nums = '123456789'
            for row in board[r_s:r_e, c_s:c_e]:
                for el in row:
                    if el not in all_nums and el != '.':
                        return False
                    all_nums = all_nums.replace(el, '')
    return True


def check_row_and_col(board):
    len_col = len(board[0])
    len_row = len(board)
    all_nums = '123456789'
    for row in range(len_row):
        temp_all_nums = all_nums
        for col in range(len_col):
            num = board[row][col]
            if num not in temp_all_nums and num != '.':
                return False
            temp_all_nums = temp_all_nums.replace(num, '')
    for col in range(len_col):
        temp_all_nums = all_nums
        for row in range(len_row):
            num = board[row][col]
            if num not in temp_all_nums and num != '.':
                return False
            temp_all_nums = temp_all_nums.replace(num, '')
    return True


print(isValidSudoku([[".",".",".",".","5",".",".","1","."],
                     [".","4",".","3",".",".",".",".","."],
                     [".",".",".",".",".","3",".",".","1"],
                     ["8",".",".",".",".",".",".","2","."],
                     [".",".","2",".","7",".",".",".","."],
                     [".","1","5",".",".",".",".",".","."],
                     [".",".",".",".",".","2",".",".","."],
                     [".","2",".","9",".",".",".",".","."],
                     [".",".","4",".",".",".",".",".","."]]

))