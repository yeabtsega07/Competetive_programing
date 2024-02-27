class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        track = set()
        
        def subsets( nums, cur = [], index = 0):
            
            if index >= len(nums):
                track.add(tuple(cur))
                return
            
            cur.append(nums[index])
            subsets(nums, cur, index + 1)
            cur.pop()
            
            subsets(nums, cur, index + 1)
        
        subsets(nums)
        
        return track