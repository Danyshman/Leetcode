class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st = []
        i = 0
        j = 0
        while i != len(pushed):
            st.append(pushed[i])
            while st and st[-1] == popped[j]:
                st.pop()
                j += 1
            i += 1
        return len(st) == 0
