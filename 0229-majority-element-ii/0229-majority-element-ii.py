class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = Counter(nums)
        
        result = []
        
        for key, val in count.items():
            
            if val > n / 3:
                result.append(key)
        
        return result
        