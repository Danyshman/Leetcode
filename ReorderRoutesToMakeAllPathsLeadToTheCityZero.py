from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        def dfs(node):
            nonlocal changes
            visited.add(node)
            is_right = False
            for i in adj_list[node]:
                is_right |= dfs(i) if i not in visited else True
            changes += 0 if is_right else 1
            return is_right

        adj_list = defaultdict(list)
        for i in connections:
            adj_list[i[0]].append(i[1])

        visited = set([0])
        changes = 0
        for route in connections:
            if route[1] == 0:
                visited.add(route[0])
        for i in range(n):
            if i not in visited:
                dfs(i)
        return changes