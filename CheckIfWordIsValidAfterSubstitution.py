class Solution:
    def isValid(self, S: str) -> bool:
        st = []
        for l in S:
            if l == 'c':
                if ''.join(st[len(st)-2:]) != 'ab' or len(st) < 2:
                    return False
                st.pop()
                st.pop()
            else:
                st.append(l)
        return len(st) == 0