class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        arr = []
        for p in S:
            if p == '(':
                arr.append(p)
            else:
                if arr[-1] == '(':
                    arr.pop()
                    if arr and arr[-1] not in ['(', ')']:
                        arr[-1] += 1
                    else:
                        arr.append(1)
                elif arr[-2] == '(':
                    num = arr.pop()*2
                    arr.pop()
                    if arr and arr[-1] not in ['(', ')']:
                        arr[-1] += num
                    else:
                        arr.append(num)
                else:
                    num = arr.pop()+arr.pop()
                    arr.pop()
                    if arr and arr[-1] not in ['(', ')']:
                        arr[-1] += num
                    else:
                        arr.append(num)
        return sum(arr)