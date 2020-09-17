class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        pasific_ocean = set()
        atlantic_ocean = set()
        if not matrix:
            return []
        h, w = len(matrix), len(matrix[0])
        visited = set()

        def dfs(r, c, visited):
            visited.add((r, c))
            for rr, cc in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
                if 0 <= rr < h and 0 <= cc < w and (rr, cc) not in visited and matrix[r][c] <= matrix[rr][cc]:
                    dfs(rr, cc, visited)

        for i in range(h):
            dfs(i, 0, pasific_ocean)
            dfs(i, w - 1, atlantic_ocean)
        for i in range(w):
            dfs(0, i, pasific_ocean)
            dfs(h - 1, i, atlantic_ocean)
        return list(pasific_ocean.intersection(atlantic_ocean))
