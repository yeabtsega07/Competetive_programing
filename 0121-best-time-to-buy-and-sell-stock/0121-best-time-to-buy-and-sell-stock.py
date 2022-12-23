class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        buy, sell = 0 , 1
        ans = 0
        
        while sell < len(prices):
            if prices[buy] > prices[sell]:
                buy = sell
                sell += 1
            else:
                ans = max(prices[sell] -  prices[buy], ans)
                sell += 1
        return ans        
        
        
        