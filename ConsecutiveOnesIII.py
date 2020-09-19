class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        cur_len = 0
        max_len = 0
        changes = 0
        start = 0
        for end in range(len(A)):
            cur_len += 1
            if not A[end]:
                changes += 1
                while changes > K:
                    cur_len -= 1
                    changes -= 1 if not A[start] else 0
                    start += 1
            max_len = max(max_len, cur_len)
        return max_len