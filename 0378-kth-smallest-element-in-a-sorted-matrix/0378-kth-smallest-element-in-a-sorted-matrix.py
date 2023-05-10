class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        min_heap = []
        for row in matrix:
            min_heap += row
        
        heapify(min_heap)
        # print(min_heap)
        
        while min_heap and k:
            
            current =  heappop( min_heap )
            k -= 1
        
        return current
        