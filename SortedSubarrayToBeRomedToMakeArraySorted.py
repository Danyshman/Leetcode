class Solution:
    def findLengthOfShortestSubarray(self, arr) -> int:
        idx1, idx2 = 0, len(arr)-1
        n, ans = len(arr), len(arr)
        while idx1 < n-1 and arr[idx1] <= arr[idx1+1]:
            idx1 += 1
        while idx2 > idx1 and arr[idx2] >= arr[idx2-1]:
            idx2 -= 1
        i, j = 0, idx2
        # ans = min(n-idx1-1, idx2)
        while i <= idx1 and j < len(arr):
            if arr[i] <= arr[j]:
                ans = min(ans, j - i - 1)
                i += 1
            else:
                j += 1
        return ans

obj = Solution()
print(obj.findLengthOfShortestSubarray([1,2,3,10,4,2,3,5]
))