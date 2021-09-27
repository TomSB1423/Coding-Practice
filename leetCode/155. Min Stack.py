class MinStack:

    def __init__(self):
        self.arr = []

    def push(self, val: int) -> None:
        mini = self.getMin()
        if val < mini:
            mini = val
        self.arr += [[val, mini]]

    def pop(self) -> None:
        self.arr = self.arr[:-1]

    def top(self) -> int:
        return self.arr[-1][0]

    def getMin(self) -> int:
        if len(self.arr):
            return self.arr[len(self.arr)-1][1]
        return float('inf')


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
