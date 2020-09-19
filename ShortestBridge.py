from collections import deque


class Solution:
    def shortestBridge(self, A) -> int:
        def dfs(r, c):
            queue.append((r, c))
            A[r][c] = 2
            for rr, cc in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
                if 0 <= rr < h and 0 <= cc < w and A[rr][cc]:
                    dfs(rr, cc)

        if not A:
            return 0
        h, w = len(A), len(A[0])
        flag = False
        visited = set()
        queue = deque()
        ans = 0
        for i in range(h):
            for j in range(w):
                if A[i][j]:
                    dfs(i, j)
                    flag = True
                    break
            if flag:
                break

        while (queue):
            for i in range(len(queue)):
                r, c = queue.popleft()
                if A[r][c] == 1:
                    return ans - 1
                for rr, cc in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
                    if 0 <= rr < h and 0 <= cc < w and (rr, cc) not in visited:
                        queue.append((rr, cc))
                        visited.add((rr, cc))
            ans += 1

obj = Solution()

print(obj.shortestBridge([[0,1],[1,0]]))