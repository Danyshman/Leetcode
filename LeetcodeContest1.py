def minCostToMoveChips(chips):
    sum = 0
    even = 0
    odd = 0
    for i in range(len(chips)):
        if chips[i] % 2 == 0:
            even += 1
        else:
            odd += 1
    return min(even, odd)


# print(minCostToMoveChips([6,4,7,8,2,10,2,7,9,7]))


# def longestSubsequence(arr, difference):
#     max_subseq = 1
#     arr1 = set(arr)
#     checked_nums = set()
#     for i in range(len(arr)-1):
#         if arr[i] in checked_nums:
#             continue
#         target = arr[i] + difference
#         temp_max = 1
#         if target not in arr1:
#             continue
#         checked_nums.add(arr[i])
#         for j in range(i+1,len(arr)):
#             if target not in arr1:
#                 break
#             if arr[j] == target:
#                 checked_nums.add(target)
#                 target += difference
#                 temp_max += 1
#         if temp_max > max_subseq:
#             max_subseq = temp_max
#     return max_subseq


# print(longestSubsequence([1,5,7,8,5,3,4,2,1], -2))


def longestSubsequence(arr, difference):
    d = dict()
    max_sub = 0
    for num in arr:
        cur = d.get(num-difference, 0) + 1
        max_sub = max(max_sub, cur)
        d[num] = cur
    return max_sub


# print(longestSubsequence([1,5,7,8,5,3,4,2,1], -2))


class Solution:
    def getMaximumGold(self, grid):
        cols, rows = len(grid), len(grid[0])
        self.ans = 0

        def dfs(x,y,presium):
            presium += grid[x][y]
            self.ans = max(presium, self.ans)
            for dx, dy in [[-1,0],[1,0],[0,-1],[0,1]]:
                nx, ny = x+dx, y+dy
                if 0<=nx<cols and 0<=ny<rows and (nx,ny) not in visited and grid[nx][ny] != 0:
                    visited.add((nx,ny))
                    dfs(nx,ny,presium)
                    visited.remove((nx,ny))

        for i in range(cols):
            for j in range(rows):
                if grid[i][j]:
                    visited = set()
                    visited.add((i,j))
                    dfs(i,j,0)
        return self.ans

# print(Solution.getMaximumGold(Solution, [[0,6,0],
#  [5,8,7],
#  [0,9,0]]))


