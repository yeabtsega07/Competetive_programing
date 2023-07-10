class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        """
        flag = 1 --> buy
        flag = 0 --> sell
        """
        
        dp = {}
        
        def recur ( index, flag ):
            
            if (index, flag) in dp:
                return dp[(index, flag)]
            
            if index >= len(prices):
                return 0
            
            if index == len(prices) - 1:
                
                return prices[index] - fee if not flag else 0
            
            
            if flag:
                take = - prices[index] + recur( index + 1, 0)
            else:
                take = prices[index] - fee + recur( index + 1, 1)
            
            notTake = recur(index + 1, flag)
            
            dp[(index, flag)] = max(take, notTake)
            
            return dp[(index, flag)]
        
        return recur( 0, 1 )
            
            
            
            
                
            
            
        