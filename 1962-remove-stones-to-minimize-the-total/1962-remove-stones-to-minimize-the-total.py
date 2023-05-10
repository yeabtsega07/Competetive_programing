class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        max_heap = [ -pile for pile in piles]
        heapify(max_heap)
        
        while max_heap and k:
            
            current = heappop(max_heap) // 2 
            heappush(max_heap, current)
            k -= 1
        

        return - sum(max_heap)