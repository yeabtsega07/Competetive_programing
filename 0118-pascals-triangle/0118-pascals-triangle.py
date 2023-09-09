class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
         
        
        dp = {1:[1], 2:[1,1]}
        
        def recur ( index ):
            if index in dp:
                return dp[index]
            
            res = [1] * index
            prev = recur(index - 1)
            for val in range(1, index - 1):
                res[val] = prev[val] + prev[val - 1]
            
            dp[index] = res
            return dp[index]
        
        recur(numRows)
        
        return list(dp.values()) if numRows > 1 else [[1]]
                
            
            
            
        