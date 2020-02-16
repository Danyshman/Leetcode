class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = []
        for i in range(len(s)):
            if s[i] in ['(', ')']:
                if s[i] == '(':
                    st.append(('(', i))
                else:
                    if st and  st[-1][0] == '(' and s[i] == ')':
                            st.pop()
                    else:
                        st.append((')', i))
        for i in st:
            s = s[0:i[1]]+ ' ' + s[i[1]+1:]
        s =s.replace(' ', '')
        return s