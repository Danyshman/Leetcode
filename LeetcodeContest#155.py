def minimumAbsDifference(arr):
    arr.sort()
    min_diff = abs(arr[0] - arr[1])
    pairs = [[arr[0], arr[1]]]
    for i in range(1,len(arr)-1):
        if abs(arr[i] - arr[i+1]) < min_diff:
            min_diff = abs(arr[i] - arr[i+1])
            pairs.clear()
            pairs.append([arr[i], arr[i+1]])
        elif abs(arr[i] - arr[i+1]) == min_diff:
            pairs.append([arr[i], arr[i+1]])

    return pairs


# print(minimumAbsDifference([40,11,26,27,-20]))


def nthUgplyNumber(n, a, b, c):
    counter = 0
    i = 1
    while counter != n:
        if (i % a == 0) or (i % b == 0) or (i % c == 0):
            counter += 1
        i += 1
    return i-1


# print(nthUgplyNumber(n = 1000000000, a = 2, b = 217983653, c = 336916467))


class Solution:
    def dfs(self, x, path):
        for t in self.d.get(x,[]):
            if t not in self.visited:
                path.add(t)
                self.visited.add(t)
                self.dfs(self, t, path)

    def smallestStringWithSwaps(self, s, pairs):
        d = dict()
        for a, b in pairs:
            if d.get(a,0) == 0:
                d[a] = [b]
            elif d.get(a,0) != 0:
                d[a].append(b)
            if d.get(b,0) == 0:
                d[b] = [a]
            elif d.get(b,0) != 0:
                d[b].append(a)

        self.visited = set()
        self.d = d
        s = list(s)
        for start in range(len(s)):
            if start not in self.visited:
                path = {start}
                self.visited.add(start)
                self.dfs(self, start, path)
                cList = [s[i] for i in path]
                cList.sort()
                path = list(path)
                path.sort()
                for i in range(len(cList)):
                    s[path[i]] = cList[i]
        return "".join(s)


print(Solution.smallestStringWithSwaps(Solution, "xwwbesrhlaoucciymqe", [[12,5],[17,8],[0,8],[8,13],[16,10],[4,15],[11,12],[2,11],[14,7],[13,18],[1,10],[4,8],[2,17],[8,1],[15,13],[16,12],[16,18],[13,11],[12,0]]))








