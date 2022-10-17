class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def helper(k):
            track=defaultdict(int)
            left,res = 0,0
            
            for right in range(len(nums)):
                track[nums[right]] += 1
                
                while len(track) > k:
                    track[nums[left]] -= 1
                    
                    if track[nums[left]] == 0:
                        track.pop(nums[left])
                    
                    left += 1
                
                res += right-left+1
            
            return res    
            
        return helper(k) - helper(k-1)    
            
        