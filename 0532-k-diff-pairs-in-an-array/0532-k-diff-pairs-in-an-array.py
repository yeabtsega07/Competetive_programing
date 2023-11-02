class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        count = Counter(nums)
        result = 0
        
        for key in count:
            
            if k == 0:
                if count[key] > 1:
                    result += 1
            else:
                if key + k in count:
                    result += 1
        
        return result