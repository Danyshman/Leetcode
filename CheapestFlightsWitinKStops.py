from collections import defaultdict, deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        matrix = defaultdict(list)
        ans = float('inf')
        stops = 0
        queue = deque([[src, 0]])
        seen = {}
        for s, e, p in flights:
            matrix[s].append([e, p])
        while queue and stops <= K+1:
            for i in range(len(queue)):
                node, price = queue[i]
                if node == dst:
                    ans = min(ans, price)
                for node2, price2 in matrix[node]:
                    if (node2 in seen and seen[node2] > price+price2) or node2 not in seen:
                        queue.append([node2, price+price2])
                        seen[node2] = price+price2
            stops += 1
        return ans if ans != float('inf') else -1