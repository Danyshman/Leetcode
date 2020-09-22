class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        count = 0
        n = len(M)
        def dfs(node):
            for i in range(n):
                if M[node][i]:
                    M[node][i] = 0
                    dfs(i)
        for i in range(n):
            if M[i][i]:
                count += 1
                dfs(i)
        return count