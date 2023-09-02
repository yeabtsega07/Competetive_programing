class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        check = set(dictionary)
        dp = {}
        dp[len(s)] = 0
        
        def recur ( index ):
            
            if index in dp:
                return dp[index]
            
            result = 1 + recur(index + 1)
            
            for j in range(index, len(s)):
                if s[index : j + 1] in check:
                    result = min(result, recur(j + 1))
            
            dp[index] = result
            return result
        
        return recur(0)           
            
        
        
        