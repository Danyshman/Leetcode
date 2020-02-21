class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        g_list = []
        for arr in matrix:
            g_list.extend(arr)
        g_list.sort()
        return g_list[k-1]