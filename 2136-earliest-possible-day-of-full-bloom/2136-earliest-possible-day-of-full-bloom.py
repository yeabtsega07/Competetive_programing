class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        track = []
        
        for i, growT in enumerate(growTime):
            
            track.append([growT,plantTime[i]])
        
        
        ans = plantT = 0
        for gtime, ptime in sorted(track, reverse = True):
            # print(gtime, ptime)
            
            check = (ptime + gtime) - (ans - plantT)
            
            if check > 0:
                ans += check
                
            plantT += ptime
            
            # print(gtime, ptime, ans, plantT)
        return ans    
        
            