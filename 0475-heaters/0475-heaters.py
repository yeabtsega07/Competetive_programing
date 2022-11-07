class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        pt1, ans = 0, 0
        houses.sort()
        heaters.sort()
        
        if houses == heaters:
            return 0
        
        for pt2 in range(len(houses)):
                
            while pt1+1 < len(heaters) and (abs(houses[pt2] - heaters[pt1]) >  abs(houses[pt2] - heaters[pt1+1])):
                
                pt1 = pt1 + 1
                
            ans = max(ans , abs(houses[pt2]-heaters[pt1]))
            
           
        return ans
                    
                    