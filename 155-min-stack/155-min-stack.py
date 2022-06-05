class MinStack:

    def __init__(self):
        self.minstack=[]
    def push(self, val: int) -> None:
        self.minstack.append(val)
    def pop(self) -> None:
        self.minstack.pop()
    def top(self) -> int:
        return self.minstack[-1]
    def getMin(self) -> int:
        return min(self.minstack)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()