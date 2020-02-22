class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        l = 0
        r = max(arr)
        ans = [r, abs(sum(arr) - target)]
        while l <= r:
            mid = l + (r - l) // 2
            temp_sum = 0
            for n in arr:
                temp_sum += mid if (n > mid) else n
            if abs(temp_sum - target) == ans[1]:
                ans[0] = min(ans[0], mid)
            if abs(temp_sum - target) < ans[1]:
                ans = [mid, abs(temp_sum - target)]
            if temp_sum > target:
                r = mid - 1
            else:
                l = mid + 1
        return ans[0]

