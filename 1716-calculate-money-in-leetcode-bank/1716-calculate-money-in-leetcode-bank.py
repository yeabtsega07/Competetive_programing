class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        for i in range(n):
            ans += (i // 7) + 1 + (i  % 7)
        
        return ans
        