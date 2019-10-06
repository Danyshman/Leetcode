def uniqueOccurrences(arr):
    d = dict()
    for num in arr:
        d[num] = d.get(num,0)+1
    unique_values = set(d.values())
    non_unique = d.values()
    return len(non_unique) == len(unique_values)


# print(uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))


def equalSubstring(s, t, maxCost):

    costs = []
    for i in range(len(s)):
        costs.append(abs(ord(s[i]) - ord(t[i])))
    cost = 0
    ans = 0
    for i in range(len(s)):
        cost += costs[i]
        if cost > maxCost:
            cost -= costs[i-ans]
        else:
            ans += 1
    return ans


# print(equalSubstring("krpgjbjjznpzdfy","nxargkbydxmsgby",14))


def removeDuplicates(s, k):
    is_there_duplicate = True
    while is_there_duplicate:
        is_there_duplicate = False
        i=0
        while True:
            if len(s) < k or i > len(s) - k:
                break
            elif s[i:i + k] == s[i] * k:
                s = s[:i] + s[i + k::]
                is_there_duplicate = True
                break
            else:
                i += 1
    return s


# print(removeDuplicates(s = "pbbcggttciiippooaais", k = 2))


class Solution:
    def minimumMoves(self, grid):
        self.ans = 0
        n = len(grid)
        visited = set()
        def dfs(tail, head, move):
            if (n-1, n-2) == tail and (n-1, n-1) == head:
                if self.ans == 0:
                    self.ans = move
                else:
                    min(self.ans, move)
            visited.add((tail, head))
            for ntail, nhead, dir in [[(tail[0] + 1, tail[1]), (head[0] + 1, head[1]), 'down'],
                                 [(tail[0], tail[1] + 1), (head[0], head[1] + 1), 'right'],
                                 [(tail[0], tail[1]), (head[0] + 1, head[1] - 1), 'clock'],
                                 [(tail[0], tail[1]), (head[0] - 1, head[1] + 1), 'counter']]:
                if 0<=ntail[0] < n and 0<=ntail[1] < n and 0<=nhead[0] < n and 0<=nhead[1] < n:
                    if dir == 'clock':
                        if grid[tail[0]+1][tail[1]] == 0 and grid[head[0]+1][head[1]] == 0 and (ntail, nhead) not in visited and tail[0] == head[0]:
                            dfs(ntail,nhead,move+1)
                    elif dir == 'counter':
                        if grid[tail[0]][tail[1]+1]== 0 and grid[head[0]][head[1]+1] == 0 and (ntail, nhead) not in visited and tail[1] == head[1]:
                            dfs(ntail,nhead, move+1)
                    elif dir == 'down' or dir == 'right':
                        if grid[ntail[0]][ntail[1]] == 0 and grid[nhead[0]][nhead[1]] == 0 and (ntail, nhead) not in visited:
                            dfs(ntail, nhead, move + 1)
        dfs((0,0),(0,1),0)
        return self.ans


print(Solution.minimumMoves(Solution, [[0,0,0,0,0,1],
                                       [1,1,0,0,1,0],
                                       [0,0,0,0,1,1],
                                       [0,0,1,0,1,0],
                                       [0,1,1,0,0,0],
                                       [0,1,1,0,0,0]]

))

