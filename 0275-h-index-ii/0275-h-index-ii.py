class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        low, high = 0, len(citations) - 1
        
        while low <= high:
            
            mid = low + (high  - low) // 2

            if citations[mid] == len(citations) - mid :
                return citations[mid]
            elif citations[mid] > len(citations) - mid :
                high = mid - 1
            else:
                low = mid + 1
        
        return len(citations) - low

        