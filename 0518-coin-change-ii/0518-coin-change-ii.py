class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        pre = [0] * (amount + 1)
        pre[0] = 1
        
        for i in range (len(coins) - 1, -1, -1):
            cur = [0] * (amount + 1)
            cur[0] = 1
            
            for a in range(1, amount + 1):
                cur[a] = pre[a]
                if a - coins[i] >= 0:
                    cur[a] += cur[a - coins[i]]
            
            pre = cur
        
        return pre[amount]
                    
        