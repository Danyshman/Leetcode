class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i==0 or j==0) and matrix[i][j] == 1:
                    count += 1
                elif matrix[i][j] == 1:
                    count += min(matrix[i][j-1],matrix[i-1][j],matrix[i-1][j-1]) + 1
                    matrix[i][j] = min(matrix[i][j-1],matrix[i-1][j],matrix[i-1][j-1]) + 1
        return count