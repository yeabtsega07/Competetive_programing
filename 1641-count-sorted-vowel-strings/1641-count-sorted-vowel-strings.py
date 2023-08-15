class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        dp = {}
        
        def recur ( index, count ):
            
            if (index, count) in dp:
                return dp[(index, count)]
            
            if count == n:
                return 1
            
            if index >= 5:
                return 0
            
            dp[(index, count)] = 0
            
            for i in range(index, 5 ):
                
                dp[(index, count)] += recur( i, count + 1 )
            
            return dp[(index, count)]
        
        return recur ( 0, 0 )
                