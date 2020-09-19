class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'o', 'u', 'i'])
        max_vowels = 0
        cur_vowels = 0
        for i in range(len(s)):
            if s[i] in vowels:
                cur_vowels += 1
            if i >=k and s[i-k] in vowels:
                cur_vowels -= 1
            max_vowels = max(max_vowels, cur_vowels)
        return max_vowels