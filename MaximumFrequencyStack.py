class FreqStack:

    def __init__(self):
        self.freq = {}
        self.st = []

    def push(self, x: int) -> None:
        self.freq[x] = self.freq.get(x, 0) + 1
        self.st.append((x, self.freq[x]))
        i = max(0, len(self.st) - 2)
        while i >= 0 and self.freq[x] < self.st[i][1]:
            self.st[i], self.st[i + 1] = self.st[i + 1], self.st[i]
            i -= 1

    def pop(self) -> int:
        self.freq[self.st[-1][0]] -= 1
        return self.st.pop()[0]

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()