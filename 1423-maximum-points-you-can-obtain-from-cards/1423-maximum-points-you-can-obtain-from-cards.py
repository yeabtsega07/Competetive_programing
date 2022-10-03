class Solution:
    def maxScore(self, card: List[int], k: int) -> int:
        pre=[1]*len(card)
        pre[0]=card[0]
        
        for i in range(1,len(card)):
            pre[i]=card[i]+pre[i-1]
        
        if k==len(card):
            return pre[len(card)-1]
       
        left=0
        right=len(card)-k-1
        max_=pre[len(card)-1]-pre[right]
        
        while right<len(card)-1:
            right+=1
            left+=1
            
            if right<len(card)-1:
                temp=pre[len(card)-1]-pre[right]+pre[left-1]
            
            else:
                temp=pre[left-1]
            
            max_=max(max_,temp)
        return max_     
            
            
            
            
        
