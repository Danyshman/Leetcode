class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        freq = {}
        cur_len = 0
        start = 0
        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i], 0) + 1
            if freq[s[i]] > cur_len:
                cur_len = freq[s[i]]
            while i - start + 1 - cur_len > k:
                freq[s[start]] -= 1
                start += 1
            max_len = max(max_len, i - start + 1)
        return max_len
