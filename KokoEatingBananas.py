import math

class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        if len(piles) == H:
            return max(piles)
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = lo + (hi-lo) // 2
            need = 0
            for p in piles:
                need += math.ceil(p/mid)
            if need > H:
                lo = mid + 1
            else:
                hi = mid
        return lo