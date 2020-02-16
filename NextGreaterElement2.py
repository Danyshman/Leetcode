class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        st = []
        for i in range(len(nums)):
            while st and nums[i] > nums[st[-1]]:
                ans[st.pop()] = nums[i]
            st.append(i)
        for i in range(len(nums[::-1])):
            while st and nums[i] > nums[st[-1]]:
                ans[st.pop()] = nums[i]
            st.append(i)
        return ans