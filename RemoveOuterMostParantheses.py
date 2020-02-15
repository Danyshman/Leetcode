class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        result = ''
        count = 0
        for p in S:
            if (count == 0 and p == '('):
                count += 1
            elif (count == 1 and p == ')'):
                count -= 1
            elif p == '(':
                count += 1
                result += p
            else:
                result += p
                count -= 1
        return result
