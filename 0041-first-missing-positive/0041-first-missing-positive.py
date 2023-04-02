class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        track = Counter(nums)
        max_ = max(nums)
        
        for i in range(1, max_ + 1):
            
            if i not in track:
                return i
        # print(i, nums)
        return max_ + 1 if max_ >= 0 else 1    
        