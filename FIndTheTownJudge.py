class Solution:
    def findJudge(self, N: int, trust):
        if N == 1:
            return 1
        judges = dict()
        trusters = []
        for person in trust:
            judges[person[1]] = judges.get(person[1],0) + 1
            trusters.append(person[0])
        for key, value in judges.items():
            if value == N-1:
                if key not in trusters:
                    return key
        return -1