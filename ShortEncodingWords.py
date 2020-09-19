class Solution:
    def minimumLengthEncoding(self, words) -> int:
        words = sorted(words, key=len, reverse=True)
        ans = 0
        partitions = dict()
        for i in range(len(words)):
            if words[i] not in partitions:
                ans += len(words[i]) + 1
                for j in range(len(words[i]) - 1, -1, -1):
                    partitions[words[i][j:]] = words[i][j:]
        return ans


obj = Solution()
print(obj.minimumLengthEncoding(["me", "time"]))
