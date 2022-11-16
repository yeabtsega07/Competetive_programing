class SmallestInfiniteSet:

    def __init__(self):
        self.nums = [i for i in range(1, 1001)]
        heapq.heapify(self.nums)
          
    def popSmallest(self) -> int:
        return heapq.heappop(self.nums)

    def addBack(self, num: int) -> None:
        if num not in self.nums:
            heapq.heappush(self.nums, num)
        
        
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)