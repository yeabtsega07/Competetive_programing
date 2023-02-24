class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.leng = k
        self.right = 0
        self.left = 0
    def enQueue(self, value: int) -> bool:
        if self.right - self.left !=  self.leng:
            self.queue[self.right % self.leng] = value
            self.right = self.right + 1 
            return True
        else:
            return False
        
    def deQueue(self) -> bool:
        if self.right != self.left:
            self.queue[self.left % self.leng] = 0
            self.left = self.left + 1 
            return True
        else:
            return False
        
    def Front(self) -> int:
        if self.left != self.right:
            return self.queue[self.left  % self.leng]
        else:
            return -1 

    def Rear(self) -> int:
        if self.left != self.right:
            return self.queue[(self.right - 1) % self.leng]
        else:
            return -1

    def isEmpty(self) -> bool:
        return self.right == self.left 

    def isFull(self) -> bool:
        return self.right - self.left == self.leng


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()