class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        collection = set()
        check = [i for i in range(left, right + 1)]
        
        for interval in ranges:
            
            for i in range(interval[0] , interval[1] + 1):
                
                collection.add(i)
                
        for num in check:
            
            if num not in collection:
                
                return False
        
        return True