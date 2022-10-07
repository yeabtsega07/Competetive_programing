class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        if len(chalk)==1:
            return 0
        pre=0
        for i,num in enumerate(chalk):    
            pre+=num
            if pre>k:
                return i
        # while k>pre:
        #     k-=pre
        k%=pre
        for i , n in enumerate(chalk):
            k-=n
            if k<0:
                return i
        if k==0:
            return 0
                
            