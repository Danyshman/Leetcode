class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.leads = self.count_votes(persons)
        self.times = times

    def q(self, t: int) -> int:
        l = 0
        r = len(self.leads) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if self.times[mid] > t:
                r = mid - 1
            else:
                l = mid + 1
        return self.leads[r]

    def count_votes(self, votes):
        temp_max = (0, 0)
        result = []
        person_votes = {}
        for vote in votes:
            person_votes[vote] = person_votes.get(vote, 0) + 1
            if person_votes[vote] >= temp_max[1]:
                temp_max = (vote, person_votes[vote])
            result.append(temp_max[0])
        return result

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)