class Solution:
    def simplifyPath(self, path) -> str:
        path = path.split('/')
        st = []
        for p in path:
            if p == '.' or p == '':
                continue
            elif p == '..' and len(st) < 2:
                st = []
            elif p == '..':
                st.pop()
            else:
                st.append('/' + p)
        return '/' if (len(st) == 0) else ''.join(st)