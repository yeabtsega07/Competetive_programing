class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        count=[1]*len(prices)
        fast,slow=1,0
        while fast<len(prices):
            if prices[slow]==prices[fast]+1:
                count[fast]=1+count[slow]
                
            slow+=1
            fast+=1    
        return sum(count)        
                
        