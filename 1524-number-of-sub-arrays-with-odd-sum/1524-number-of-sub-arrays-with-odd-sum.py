class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        ans = 0
        ev,od = 0,0
        
        for num in arr:
            if num % 2 == 0:
                ev , od = ev+1,od
            else:
                ev , od = od , ev+1
            ans = (ans + od) %(10**9 + 7) 
        return ans   
            

            