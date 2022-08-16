class MyStack:

    def __init__(self):
        self.queue=[]
        self.rear=0

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.rear+=1

    def pop(self) -> int:
        # if  self.empty:
        #     top_elm=self.queue[self.rear-1]
        #     self.queue.remove(top_elm)
        self.rear-=1
        #     return top_elm
        return self.queue.pop()

    def top(self) -> int:
        return self.queue[self.rear-1]        

    def empty(self) -> bool:
        return self.rear==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()