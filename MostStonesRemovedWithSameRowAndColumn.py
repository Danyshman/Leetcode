class Solution:
    def removeStones(self, stones):
        if not stones:
            return 0
        am = dict()
        for r,c in stones:
            for rr,cc in stones:
                if (abs(r - rr) == 1 and (c - cc) == 0) or (abs(c - cc) == 1 and (r - rr) == 0):
                    if am.get((r, c), False):
                        am[(r, c)].append((rr, cc))
                    else:
                        am[(r, c)] = [(rr, cc)]
        return max([self.dfs(am, key, set([key])) for key, value in am.items()])
    def dfs(self, am, start,visited):
        max_stones = 1
        for rr,cc in am[start]:
            if (rr,cc) not in visited:
                visited.add((rr,cc))
                max_stones = max(max_stones, self.dfs(am, (rr,cc), visited)+1)
        return max_stones


obj = Solution()
print(obj.removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]))