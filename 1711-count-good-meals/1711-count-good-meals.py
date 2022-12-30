class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        """
        0 <= deliciousness[i] <= 2**20
        which means the max value that the power of 2 can get is 2**20 so 
        the max pair sum would be 2**20 + 2**20 which would be 2**21
        from 2**0 to 2**21
        22 possibilities
        """
        track, ans, mod = defaultdict(int), 0, 10**9 + 7
        
        for meal in deliciousness:
            
            for i in range(22):    
                ans += track[2**i - meal]
                
            track[meal] += 1
        
        return  ans % mod 
            
            
        
        

                    
            