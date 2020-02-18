class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for a in asteroids:
            if st and a < 0:
                while st and st[-1] > 0 and abs(a) > st[-1]:
                    st.pop()
                if st and st[-1] > 0 and abs(a) == st[-1]:
                    st.pop()
                    continue
                if not st or st[-1] < 0:
                    st.append(a)
                continue
            st.append(a)
        return st