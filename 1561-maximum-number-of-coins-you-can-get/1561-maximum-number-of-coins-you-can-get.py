class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        res=0
        i=len(piles)//3
        while i<len(piles):
            res+=piles[i]
            i+=2
  
        return res        
        