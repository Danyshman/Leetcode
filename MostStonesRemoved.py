from collections import defaultdict
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        visited = set()
        count = 0
        def dfs(r, c):
            visited.add((r,c))
            for rr, cc in stones:
                if (rr == r or cc == c) and (rr,cc) not in visited:
                    dfs(rr,cc)
        for r,c in stones:
            if (r,c) not in visited:
                count += 1
                dfs(r,c)
        return len(stones) - count