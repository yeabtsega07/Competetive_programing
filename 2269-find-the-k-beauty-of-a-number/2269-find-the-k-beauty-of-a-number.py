class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num=str(num)
        rgt=0
        div=""
        res=0
        while rgt<len(num):
            div+=num[rgt]
            if len(div)==k:
                if int(div)!=0 and int(num)%int(div)==0:
                    res+=1
                div=div[1:]
            rgt+=1 
            
        return res     
                
                
                    
                
        