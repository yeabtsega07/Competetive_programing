class Solution:
    def maxScore(self, card: List[int], k: int) -> int:
        
        
       
        left,right=0,len(card)-k
        total=0
        for i in range(right,len(card)):
            total+=card[i]
            
        max_=total

        while right<len(card):
            
            total+=(card[left]-card[right])
            max_=max(max_,total)
            right+=1
            left+=1
            
        return max_     
            
            
            
            
        
