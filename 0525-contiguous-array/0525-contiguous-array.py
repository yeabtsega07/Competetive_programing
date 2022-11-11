class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        track  = {0:-1}
        res, cnt = 0, 0
        
        for i, num in enumerate(nums):
        
            if num == 0:
                cnt -= 1
            else:
                cnt += 1
            
            if cnt in track.keys():
                res = max(res, i - track[cnt])
            else:
                track[cnt] = i
        
        return res
                
            
            

                
        