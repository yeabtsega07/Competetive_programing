class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        track  = set()
        l, res = 0, 0
        curSum = 0
        
        for r in range(len(nums)):
            
            while nums[r] in track:
                
                track.remove(nums[l])
                curSum -= nums[l]
                l += 1
           
            
            track.add(nums[r])
            curSum += nums[r]
            res = max(res , curSum)
            
        return res     