class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        st = []
        for p in S:
            if not st or p == '(':
                st.append(p)
            else:
                if st[-1] == '(' and p == ')':
                    st.pop()
                else:
                    st.append(p)
        return len(st)