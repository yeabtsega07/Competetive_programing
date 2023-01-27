class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class MyLinkedList:

    def __init__(self):
        
        self.head = Node(0)
        self.size = 0
    def get(self, index: int) -> int:
        
        if index < 0 or index > self.size-1:
            return -1
        
        node=self.head
        for i in range(index+1):
            node = node.next
        return node.data   

    def addAtHead(self, val: int) -> None:
        
        return self.addAtIndex(0 , val)

    def addAtTail(self, val: int) -> None:
        
        return self.addAtIndex(self.size, val)
    
    def addAtIndex(self, index: int, val: int) -> None:
        
        if index > self.size:
            return
        self.size += 1
        pre = self.head
        for i in range(index):
            pre = pre.next
        newNode = Node(val) 
        newNode.next = pre.next
        pre.next = newNode
        
        return
    
    def deleteAtIndex(self, index: int) -> None:
        
        if index < 0 or index > self.size-1:
            return
        self.size -= 1
        pre=self.head
        for i in range(index):
            pre = pre.next
        pre.next = pre.next.next
        return
    

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)