class MinStack:

    def __init__(self):
        self.items = []

    def push(self, x: int) -> None:
        self.items.append(x)

    def pop(self) -> None:
        self.items.pop()

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return min(self.items)

obj = MinStack()
obj.push(2)
obj.top()
obj.getMin()
obj.push(5)
obj.pop()
