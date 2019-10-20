class NumArray:

    def __init__(self, nums):
        self.d = dict()
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        if self.d.get((i,j),False) is False:
            self.d[(i,j)] = sum(self.nums[i:j+1])
            return self.d[(i,j)]
        else:
            return self.d[(i,j)]

obj = NumArray([-2, 0, 3, -5, 2, -1])
print(obj.sumRange(0,5))