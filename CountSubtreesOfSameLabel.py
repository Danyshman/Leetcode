from collections import defaultdict, Counter

class Solution:
    def countSubTrees(self, n: int, edges, labels: str):
        def dfs(node):
            visited.add(node)
            counter = Counter([labels[node]])
            for child in graph[node]:
                if child not in visited:
                    counter += dfs(child)
            ans[node] = counter[labels[node]]

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = {}
        ans = [0]*n; dfs(0)
        return ans


obj = Solution()

print(obj.countSubTrees(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels = "abaedcd"))