class Solution:
    def generateMatrix(self, n: int):
        matrix = [[0] * n for _ in range(n)]
        ub = -1
        bb = n
        rb = n
        lb = -1
        count = 1
        r, c = 0, 0
        while count <= n * n:
            while c < rb and c < n:
                matrix[r][c] = count
                count += 1
                c += 1
            ub += 1
            r += 1
            c -= 1
            while r < bb and r < n:
                matrix[r][c] = count
                count += 1
                r += 1
            rb -= 1
            c -= 1
            r -= 1
            while c > lb and c >= 0:
                matrix[r][c] = count
                count += 1
                c -= 1
            bb -= 1
            r -= 1
            c += 1
            while r > ub and r >= 0:
                matrix[r][c] = count
                count += 1
                r -= 1
            lb += 1
            c += 1
            r += 1
        return matrix

obj = Solution()
print(obj.generateMatrix(3))
