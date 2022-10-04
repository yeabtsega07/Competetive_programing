class Solution:
    def frequencySort(self, s: str) -> str:
        count={}
        ans=""
        for i in s:
            if i not in count:
                count[i]=1
            else:
                count[i]+=1
        for i in sorted(count.items(),key=lambda x:x[1],reverse=True):
              ans+=i[0]*i[1]
        return ans    
   
        
        
            
                
        