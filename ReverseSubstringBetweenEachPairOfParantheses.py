class Solution:
    def reverseParentheses(self, s: str) -> str:
        open = []
        for i in range(len(s)):
            if s[i] == '(':
                open.append(i+1)
            elif s[i] == ')':
                s = s[:open[-1]] + s[open.pop():i][::-1] + s[i:]
        s = s.replace('(', '')
        s = s.replace(')', '')
        return s