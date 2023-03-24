class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        track = []
        
        def subsets( nums, cur = [], index = 0):
            
            if index >= len(nums):
                if len(cur) >= 2:
                    track.append(cur[:])
                return
            
            cur.append(nums[index])
            subsets(nums, cur, index + 1)
            cur.pop()
            
            subsets(nums, cur, index + 1)
        
        subsets(nums)
        
        result = set()
        
        for cur in track:
            
            if cur == sorted(cur):
                result.add(tuple(cur))
        
        return result
        
        