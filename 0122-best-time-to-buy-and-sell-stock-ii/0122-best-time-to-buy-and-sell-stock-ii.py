class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = {}
        
        def recur ( index, check ):
            
            if index >= len(prices):
                return 0
            
            if (index, check) in dp:
                return dp[(index, check)]
            
            cur = 0
            if check:
                
                
                sell = prices[index]  + recur( index + 1, 0 ) 
                notSell = recur( index + 1, 1 )
                
                cur += max(sell, notSell)
            
            else:
                
                buy = -prices[index] + recur(index + 1, 1) 
                notBuy = recur(index + 1, 0)

                cur += max(buy, notBuy)
            
            dp[(index, check)] = cur
            
            return cur
        
        return recur( 0, 0 )
                