class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.st = []
        self.min_val = []

    def push(self, x: int) -> None:
        if not self.min_val or self.min_val[-1] >= x:
            self.min_val.append(x)
        self.st.append(x)

    def pop(self) -> None:
        if self.top() == self.min_val[-1]:
            self.st.pop()
            self.min_val.pop()
        else:
            self.st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        if self.min_val:
            return self.min_val[-1]
        return 0

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()