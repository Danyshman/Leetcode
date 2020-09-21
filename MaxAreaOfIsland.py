class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r,c):
            grid[r][c] = 0
            count = 1
            for rr,cc in [[r+1, c], [r-1,c], [r, c+1], [r, c-1]]:
                if 0 <= rr < h and 0 <= cc < w and grid[rr][cc]:
                    count += dfs(rr,cc)
            return count
        if not grid:
            return 0
        h, w = len(grid), len(grid[0])
        max_area = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j]:
                    max_area = max(max_area, dfs(i, j))
        return max_area