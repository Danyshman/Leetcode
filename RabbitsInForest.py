from collections import defaultdict
class Solution:
    def numRabbits(self, answers) -> int:
        count = defaultdict(lambda: 0)
        n = len(answers)
        ans = 0
        for i in range(n):
            if answers[i] == 0:
                ans += 1
            elif answers[i] in count:
                count[answers[i]] -= 1
                if count[answers[i]] == 0:
                    count.pop(answers[i])
            else:
                ans += answers[i] + 1
                count[answers[i]] = answers[i]
        return ans

obj = Solution()
print(obj.numRabbits([0,0,1,1,1]))