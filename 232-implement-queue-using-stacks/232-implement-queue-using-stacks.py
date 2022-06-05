class MyQueue:

    def __init__(self):
        self.name=""
        self.queue=[]
    def push(self, x: int) -> None:
        self.queue.append(x)
        print(self.queue)
    def pop(self) -> int:
        if self.queue:
            return self.queue.pop(0)
    def peek(self) -> int:
        print(self.queue[0])
        return self.queue[0]
    def empty(self) -> bool:
        if not self.queue:
            return True
        else:
            return False 

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()