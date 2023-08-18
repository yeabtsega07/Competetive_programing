class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        dp = {}
        
        def recur ( index1, index2 ):
            
            if (index1, index2) in dp:
                return dp[(index1, index2)]
            
            if index1 > index2:
                return 0
            
            if index1 == index2:
                return 1
            
            take, notTake = 0, 0

            if s[index1] == s[index2]:
                take = 2 + recur(index1 + 1, index2 - 1)
            
            else:
                notTake = max(recur(index1 + 1, index2), recur(index1, index2 - 1))
                
            dp[(index1, index2)] = max(take, notTake)
            
            return max(take, notTake)
        
        return recur(0, len(s) - 1)
        