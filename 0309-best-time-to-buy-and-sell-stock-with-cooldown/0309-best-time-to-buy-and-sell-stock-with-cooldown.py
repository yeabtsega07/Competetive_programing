class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def helper(ind, buy):
            if ind >= len(prices):
                return 0
            
            profit = 0
            if buy:
                profit += max(-prices[ind] + helper(ind + 1, 0),
                             0 + helper(ind + 1, 1))
            else:
                profit += max(prices[ind] + helper(ind + 2, 1),
                             0 + helper(ind + 1, 0))
            return profit
        return helper(0, 1)
                
                
        